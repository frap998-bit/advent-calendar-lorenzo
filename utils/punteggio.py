
import streamlit as st
from supabase import create_client


# =========================================================
# COLLEGAMENTO A SUPABASE
# =========================================================

@st.cache_resource
def get_supabase():
    """
    Crea il client una sola volta e lo riutilizza
    nelle successive esecuzioni dell'app.
    """
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]

    return create_client(url, key)


# =========================================================
# INIZIALIZZAZIONE DELLO STATO LOCALE
# =========================================================

def inizializza_punteggio(forza_aggiornamento=False):
    """
    Carica i dati da Supabase soltanto se necessario.

    forza_aggiornamento=True:
        rilegge i dati dal database.

    forza_aggiornamento=False:
        usa i dati già presenti nella sessione.
    """

    if (
        not forza_aggiornamento
        and "punteggio" in st.session_state
        and "giorni_completati" in st.session_state
    ):
        return

    try:
        supabase = get_supabase()

        risposta = (
            supabase
            .table("punteggio")
            .select("giorno, punti, completato")
            .execute()
        )

        dati = risposta.data or []

        dati_completati = [
            riga
            for riga in dati
            if riga.get("completato") is True
        ]

        st.session_state.punteggio = sum(
            int(riga.get("punti") or 0)
            for riga in dati_completati
        )

        st.session_state.giorni_completati = {
            int(riga["giorno"])
            for riga in dati_completati
        }

    except Exception as e:
        st.error("Errore durante il caricamento del punteggio.")
        st.code(str(e))

        # Inizializza lo stato solo se non esiste già,
        # evitando di cancellare dati validi in memoria.
        if "punteggio" not in st.session_state:
            st.session_state.punteggio = 0

        if "giorni_completati" not in st.session_state:
            st.session_state.giorni_completati = set()


# =========================================================
# RECUPERA IL PUNTEGGIO
# =========================================================

def get_punteggio():
    """
    Restituisce il punteggio dalla sessione.
    Non effettua richieste al database se già caricato.
    """

    inizializza_punteggio()

    return st.session_state.punteggio


# =========================================================
# CONTROLLA SE UN GIORNO È COMPLETATO
# =========================================================

def giorno_completato(giorno):
    """
    Controlla lo stato in memoria.
    Non interroga Supabase per ogni casella del calendario.
    """

    inizializza_punteggio()

    return int(giorno) in st.session_state.giorni_completati


# =========================================================
# AGGIUNGI PUNTI E COMPLETA UN GIORNO
# =========================================================

def aggiungi_punti(giorno, punti):
    """
    Salva il completamento su Supabase e aggiorna
    il punteggio locale.

    Restituisce:
        True  = salvataggio riuscito
        False = giorno già completato o errore
    """

    giorno = int(giorno)
    punti = int(punti)

    try:
        # Verifica lo stato reale prima di salvare,
        # per evitare di assegnare punti due volte.
        inizializza_punteggio(forza_aggiornamento=True)

        if giorno in st.session_state.giorni_completati:
            return False

        supabase = get_supabase()

        risposta = (
            supabase
            .table("punteggio")
            .update({
                "completato": True,
                "punti": punti
            })
            .eq("giorno", giorno)
            .eq("completato", False)
            .execute()
        )

        # Se non è stata aggiornata alcuna riga,
        # il salvataggio non è confermato.
        if not risposta.data:
            inizializza_punteggio(forza_aggiornamento=True)

            st.warning(
                f"Il Giorno {giorno} non è stato salvato. "
                "Controlla la riga corrispondente in Supabase."
            )

            return False

        # Aggiorna immediatamente lo stato locale.
        # Evita un'ulteriore lettura del database.
        st.session_state.giorni_completati.add(giorno)

        st.session_state.punteggio += punti

        return True

    except Exception as e:
        st.error("Errore durante il salvataggio su Supabase:")
        st.code(str(e))

        # Tenta di riallineare lo stato con il database.
        try:
            inizializza_punteggio(forza_aggiornamento=True)
        except Exception:
            pass

        return False


# =========================================================
# RESET COMPLETO DEL CALENDARIO
# =========================================================

def reset_punteggio():
    """
    Azzera i punti e il completamento di tutti i giorni.
    """

    try:
        supabase = get_supabase()

        (
            supabase
            .table("punteggio")
            .update({
                "completato": False,
                "punti": 0
            })
            .neq("giorno", 0)
            .execute()
        )

        # Aggiorna subito la sessione.
        st.session_state.punteggio = 0
        st.session_state.giorni_completati = set()

        # Pulisce gli eventuali risultati temporanei
        # dei minigiochi per evitare schermate obsolete.
        chiavi_da_rimuovere = [
            chiave
            for chiave in st.session_state.keys()
            if chiave.startswith("giorno")
            and chiave != "giorno_aperto"
        ]

        for chiave in chiavi_da_rimuovere:
            del st.session_state[chiave]

        return True

    except Exception as e:
        st.error("Errore durante il reset del punteggio:")
        st.code(str(e))

        return False
