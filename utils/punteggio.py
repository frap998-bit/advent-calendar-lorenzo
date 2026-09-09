import streamlit as st


def inizializza_punteggio():
    if "punteggio" not in st.session_state:
        st.session_state.punteggio = 0


def aggiungi_punti(punti):
    st.session_state.punteggio += punti


def get_punteggio():
    return st.session_state.punteggio
