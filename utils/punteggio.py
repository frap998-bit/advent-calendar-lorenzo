
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

    # Se il giorno è già stato completato,
    # non assegna nuovamente i punti
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
            .execute()
        )

        # Controlla che Supabase abbia aggiornato
        # effettivamente una riga
        if not risposta.data:

            st.error(
                f"⚠️ Nessuna riga aggiornata per il Giorno {giorno}."
            )

            st.write(
                "Controlla che il Giorno "
                f"{giorno} esista nella tabella 'punteggio'."
            )

            return False

        # Aggiorna il punteggio nella sessione
        st.session_state.punteggio += punti

        # Memorizza il giorno come completato
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
# CONTROLLA SE IL GIORNO
# È GIÀ STATO COMPLETATO
# -------------------------

def giorno_completato(giorno):

    inizializza_punteggio()

    return giorno in st.session_state.giorni_completati


# -------------------------
# RESET COMPLETO
# -------------------------

def reset_punteggio():

    supabase = get_supabase()

    try:

        risposta = (
            supabase
            .table("punteggio")
            .update({
                "completato": False,
                "punti": 0
            })
            .neq("giorno", 0)
            .execute()
        )

        # Reset della sessione Streamlit
        st.session_state.punteggio = 0
        st.session_state.giorni_completati = set()

        return True

    except Exception as e:

        st.error(
            "❌ Errore durante il reset del punteggio:"
        )

        st.code(str(e))

        return False

