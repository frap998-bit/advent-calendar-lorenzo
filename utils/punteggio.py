
import streamlit as st
from supabase import create_client


# =========================================================
# COLLEGAMENTO A SUPABASE
# =========================================================

@st.cache_resource
def get_supabase():
    """
    Crea il client Supabase una sola volta
    e lo riutilizza nelle successive esecuzioni.
    """
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]

    return create_client(url, key)


# =========================================================
# CARICAMENTO DATI CON CACHE
# =========================================================

@st.cache_data(ttl=60)
def carica_dati_punteggio():
    """
    Recupera i dati da Supabase.

    La cache dura 60 secondi e viene invalidata
    dopo un salvataggio o un reset.
    """
    risposta = (
        get_supabase()
        .table("punteggio")
        .select("giorno, punti, completato")
        .execute()
    )

    return risposta.data or []


def invalida_cache_punteggio():
    """
    Forza una nuova lettura dei dati alla prossima richiesta.
    """
    carica_dati_punteggio.clear()


# =========================================================
# AGGIORNAMENTO DELLO STATO LOCALE
# =========================================================

def inizializza_punteggio(forza_aggiornamento=False):
    """
    Inizializza il punteggio nella sessione Streamlit.

    forza_aggiornamento=True:
        forza una nuova lettura da Supabase.

    forza_aggiornamento=False:
        utilizza i dati già presenti nella sessione.
    """

    if (
        not forza_aggiornamento
        and "punteggio" in st.session_state
        and "giorni_completati" in st.session_state
    ):
        return

    if forza_aggiornamento:
        invalida_cache_punteggio()

    try:
        dati = carica_dati_punteggio()

        dati_completati = [
            riga
            for riga in dati
            if riga.get("completato") is True
        ]

        punteggio = sum(
            int(riga.get("punti") or 0)
            for riga in dati_completati
        )

        giorni_completati = {
            int(riga["giorno"])
            for riga in dati_completati
        }

        st.session_state.punteggio = punteggio
        st.session_state.giorni_completati = giorni_completati

    except Exception as e:
        st.error("Errore durante il caricamento del punteggio.")
        st.code(str(e))

        # Non sovrascrive eventuali dati validi già in memoria.
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
    Non interroga il database a ogni chiamata.
    """
    inizializza_punteggio()

    return st.session_state.punteggio


# =========================================================
# CONTROLLA SE UN GIORNO È COMPLETATO
# =========================================================

def giorno_completato(giorno):
    """
    Controlla lo stato in memoria.
    Non esegue richieste a Supabase per ogni casella.
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
        # Verifica lo stato aggiornato prima del salvataggio.
        inizializza_punteggio(forza_aggiornamento=True)

        if giorno in st.session_state.giorni_completati:
            return False

        risposta = (
            get_supabase()
            .table("punteggio")
            .update({
                "completato": True,
                "punti": punti
            })
            .eq("giorno", giorno)
            .eq("completato", False)
            .execute()
        )

        if not risposta.data:
            # Rilegge i dati reali dal database.
            inizializza_punteggio(forza_aggiornamento=True)

            st.warning(
                f"Il Giorno {giorno} non è stato salvato. "
                "Verifica che esista una riga per questo giorno "
                "e che non sia già completato."
            )

            return False

        # Aggiorna la cache e lo stato locale.
        invalida_cache_punteggio()

        st.session_state.giorni_completati.add(giorno)
        st.session_state.punteggio += punti

        return True

    except Exception as e:
        st.error("Errore durante il salvataggio su Supabase.")
        st.code(str(e))

        # Tenta di riallineare la sessione con il database.
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
    Azzera il calendario su Supabase e aggiorna
    lo stato locale della sessione.
    """

    try:
        risposta = (
            get_supabase()
            .table("punteggio")
            .update({
                "completato": False,
                "punti": 0
            })
            .neq("giorno", 0)
            .execute()
        )

        # Invalida i dati memorizzati in cache.
        invalida_cache_punteggio()

        # Aggiorna immediatamente lo stato locale.
        st.session_state.punteggio = 0
        st.session_state.giorni_completati = set()

        # Rimuove gli stati temporanei dei minigiochi.
        for chiave in list(st.session_state.keys()):
            if (
                chiave.startswith("giorno")
                and chiave != "giorno_aperto"
            ):
                del st.session_state[chiave]

        return True

    except Exception as e:
        st.error("Errore durante il reset del punteggio.")
        st.code(str(e))
        return False

