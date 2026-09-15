
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(5):
        st.success("✅ Giorno 5 completato!")
        st.write("🏆 Hai già conquistato i 5 punti di questa sfida.")
        return


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("❤️ Giorno 5 — Ti ricordi le scemate che inventi?")


    st.write(
        "### ❤️ Cosa mi hai detto per farmi capire che volevi fare l'amore con me?"
    )


    # -------------------------
    # RISPOSTE
    # -------------------------

    risposta = st.radio(
        "Scegli una risposta:",
        [
            "A. «Legambiente ha organizzato la serata nazionale della spazzata contro l'inquinamento urbano»",

            "B. «La LIPU ha organizzato la serata nazionale della raccolta contro l'inquinamento urbano»",

            "C. «Il Club alpino ha organizzato la serata nazionale della spazzata contro l'inquinamento urbano»",

            "D. «Legambiente ha organizzato la serata nazionale della spazzata dei rifiuti ambientali»"
        ],
        key="giorno05_risposta"
    )


    st.write("")


    # -------------------------
    # CONTROLLO RISPOSTA
    # -------------------------

    if st.button(
        "🔎 Conferma risposta",
        use_container_width=True
    ):

        if risposta.startswith("A."):

            punti_assegnati = aggiungi_punti(5, 5)

            st.success(
                "🎉 Esatto! Direi che questo ricordo te lo sei guadagnato! ❤️"
            )

            st.balloons()

            if punti_assegnati:
                st.write(
                    "🏆 **Hai conquistato 5 punti!**"
                )

        else:

            aggiungi_punti(5, 0)

            st.error(
                "❌ Sbagliato! Hai perso i 5 punti di questa sfida."
            )

            st.info(
                "💡 La risposta corretta era: "
                "**A. «Legambiente ha organizzato la serata nazionale "
                "della spazzata contro l'inquinamento urbano»**"
            )
