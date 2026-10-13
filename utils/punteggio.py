
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
        .execute()
    )

    dati = risposta.data or []

    # Considera soltanto i giorni completati
    dati_completati = [
        riga for riga in dati
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


# -------------------------
# AGGIUNGI PUNTI
# -------------------------

def aggiungi_punti(giorno, punti):

    try:
        # Controlla lo stato reale prima di assegnare i punti.
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

        if not risposta.data:
            # Potrebbe essere già stato completato
            # oppure la riga potrebbe non esistere.
            inizializza_punteggio(forza_aggiornamento=True)

            st.warning(
                f"Il Giorno {giorno} non è stato aggiornato. "
                "Controlla la relativa riga in Supabase."
            )
            return False

        # Aggiorna il punteggio locale dopo il salvataggio.
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

    # Usa i dati già caricati in sessione:
    # nessuna richiesta a Supabase per ogni casella.
    inizializza_punteggio()

    return giorno in st.session_state.giorni_completati


# -------------------------
# RESET COMPLETO
# -------------------------

def reset_punteggio():

    try:
        supabase = get_supabase()

        supabase.table("punteggio").update({
            "completato": False,
            "punti": 0
        }).neq("giorno", 0).execute()

        st.session_state.punteggio = 0
        st.session_state.giorni_completati = set()

        return True

    except Exception as e:
        st.error("Errore durante il reset del punteggio:")
        st.code(str(e))
        return False
