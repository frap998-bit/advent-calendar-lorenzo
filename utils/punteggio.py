
import streamlit as st
from supabase import create_client


# -------------------------
# COLLEGAMENTO A SUPABASE
# -------------------------

def get_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)


# -------------------------
# CARICAMENTO DA SUPABASE
# -------------------------

def inizializza_punteggio(forza_aggiornamento=False):

    # Se i dati sono già in sessione e non è richiesto
    # un aggiornamento, non interroga nuovamente Supabase.
    if (
        "punteggio" in st.session_state
        and "giorni_completati" in st.session_state
        and not forza_aggiornamento
    ):
        return

    supabase = get_supabase()

    risposta = (
        supabase
        .table("punteggio")
        .select("giorno, punti, completato")
        .eq("completato", True)
        .execute()
    )

    dati = risposta.data or []

    st.session_state.punteggio = sum(
        int(riga.get("punti") or 0)
        for riga in dati
    )

    st.session_state.giorni_completati = {
        riga["giorno"] for riga in dati
    }


# -------------------------
# AGGIUNGI PUNTI
# -------------------------

def aggiungi_punti(giorno, punti):

    inizializza_punteggio(forza_aggiornamento=True)

    if giorno in st.session_state.giorni_completati:
        return False

    supabase = get_supabase()

    try:
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

        if not risposta.data:
            # Aggiorna lo stato locale per evitare
            # che rimanga diverso da quello del database.
            inizializza_punteggio(forza_aggiornamento=True)

            st.warning(
                f"Il Giorno {giorno} non è stato aggiornato. "
                "Verifica che esista in Supabase e che "
                "completato sia FALSE."
            )
            return False

        # Ricarica il totale reale dal database.
        inizializza_punteggio(forza_aggiornamento=True)

        return True

    except Exception as e:
        st.error("Errore durante il salvataggio su Supabase:")
        st.code(str(e))
        return False


# -------------------------
# RECUPERA PUNTEGGIO
# -------------------------

def get_punteggio():
    inizializza_punteggio()
    return st.session_state.punteggio


# -------------------------
# CONTROLLA COMPLETAMENTO
# -------------------------

def giorno_completato(giorno):

    # Rilegge sempre lo stato aggiornato da Supabase.
    inizializza_punteggio(forza_aggiornamento=True)

    return giorno in st.session_state.giorni_completati


# -------------------------
# RESET COMPLETO
# -------------------------

def reset_punteggio():

    supabase = get_supabase()

    try:
        supabase.table("punteggio").update({
            "completato": False,
            "punti": 0
        }).neq("giorno", 0).execute()

        # Svuota lo stato locale.
        st.session_state.punteggio = 0
        st.session_state.giorni_completati = set()

        return True

    except Exception as e:
        st.error("Errore durante il reset del punteggio:")
        st.code(str(e))
        return False
