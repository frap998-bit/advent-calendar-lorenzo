import streamlit as st


def inizializza_punteggio():
    if "punteggio" not in st.session_state:
        st.session_state.punteggio = 0

    if "giorni_completati" not in st.session_state:
        st.session_state.giorni_completati = set()


def aggiungi_punti(giorno, punti):
    inizializza_punteggio()

    # I punti vengono assegnati una sola volta
    if giorno not in st.session_state.giorni_completati:
        st.session_state.punteggio += punti
        st.session_state.giorni_completati.add(giorno)
        return True

    return False


def get_punteggio():
    inizializza_punteggio()
    return st.session_state.punteggio


def giorno_completato(giorno):
    inizializza_punteggio()
    return giorno in st.session_state.giorni_completati
