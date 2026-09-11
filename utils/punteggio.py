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
# INIZIALIZZAZIONE
# -------------------------

def inizializza_punteggio():

    if "punteggio" not in st.session_state:

        supabase = get_supabase()

        # Legge tutti i giorni completati
        risposta = (
            supabase
            .table("punteggio")
            .select("giorno, punti, completato")
            .eq("completato", True)
            .execute()
        )

        dati = risposta.data

        st.session_state.punteggio = sum(
            riga["punti"] for riga in dati
        )

        st.session_state.giorni_completati = {
            riga["giorno"] for riga in dati
        }


# -------------------------
# AGGIUNGI PUNTI
# -------------------------

def aggiungi_punti(giorno, punti):

    inizializza_punteggio()

    # Se il giorno è già stato completato,
    # non assegna nuovamente i punti
    if giorno in st.session_state.giorni_completati:
        return False

    supabase = get_supabase()

    # Salva il completamento su Supabase
    supabase.table("punteggio").update({
        "completato": True,
        "punti": punti
    }).eq("giorno", giorno).execute()

    # Aggiorna anche la sessione attuale
    st.session_state.punteggio += punti
    st.session_state.giorni_completati.add(giorno)

    return True


# -------------------------
# RECUPERA PUNTEGGIO
# -------------------------

def get_punteggio():

    inizializza_punteggio()

    return st.session_state.punteggio


# -------------------------
# CONTROLLA SE COMPLETATO
# -------------------------

def giorno_completato(giorno):

    inizializza_punteggio()

    return giorno in st.session_state.giorni_completati
