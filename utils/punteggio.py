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

    # Controlla se il giorno è già stato completato
    if giorno in st.session_state.giorni_completati:
        return False

    supabase = get_supabase()

    try:

        # Aggiorna la riga su Supabase
        risposta = (
            supabase
            .table("punteggio")
            .update({
                "completato": True,
                "punti": punti
            })
            .eq("giorno", giorno)
            .execute()
        )

        # Controlla che Supabase abbia effettivamente
        # restituito una riga aggiornata
        if not risposta.data:

            st.error(
                "⚠️ Supabase non ha aggiornato nessuna riga."
            )

            st.write(
                "Controlla che il Giorno "
                f"{giorno} esista nella tabella 'punteggio'."
            )

            return False

        # Aggiorna la sessione
        st.session_state.punteggio += punti
        st.session_state.giorni_completati.add(giorno)

        return True

    except Exception as e:

        st.error(
            "❌ Errore durante il salvataggio su Supabase:"
        )

        st.code(str(e))

        return False


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
