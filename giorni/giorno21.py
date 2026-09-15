import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(21):
        st.success("✅ Giorno 21 completato!")
        st.write(
            "🏆 Hai già completato questa sfida."
        )
        return


    # -------------------------
    # INIZIALIZZAZIONE
    # -------------------------

    if "giorno21_tentativi" not in st.session_state:
        st.session_state.giorno21_tentativi = 0

    if "giorno21_errore" not in st.session_state:
        st.session_state.giorno21_errore = False

    if "giorno21_finito" not in st.session_state:
        st.session_state.giorno21_finito = False


    tentativi = st.session_state.giorno21_tentativi


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("🔐 Giorno 21 — La parola misteriosa")

    st.write(
        "C'è una parola che è stata nominata alcune volte "
        "durante la scorsa estate."
    )

    st.write(
        "Hai **3 tentativi** per indovinarla."
    )

    st.info(
        "🎯 Se indovini la parola conquisti **4 punti**. "
        "Dopo 2 tentativi sbagliati si sbloccherà un nuovo indizio..."
    )


    # -------------------------
    # INDIZI
    # -------------------------

    st.subheader("💡 Gli indizi")

    st.write("☀️ **1. Animale**")

    st.write("😂 **2. Plurale**")

    st.write("🎨 **3. Coda**")

    if tentativi >= 2:
        st.write("🍦 **4. Omar e Sofia**")
    else:
        st.write("❓ **4. -**")


    # -------------------------
    # GIOCO GIÀ FINITO
    # -------------------------

    if st.session_state.giorno21_finito:

        st.divider()

        st.error(
            "😂 Hai esaurito i 3 tentativi!"
        )

        st.write(
            "💡 La parola misteriosa era:"
        )

        st.success(
            "🍪 **TOPI**"
        )

        st.write(
            "🏆 **Hai conquistato 0 punti.**"
        )

        return


    # -------------------------
    # DOPO UN ERRORE
    # -------------------------

    if st.session_state.giorno21_errore:

        st.divider()

        if tentativi == 1:

            st.warning(
                "❌ Nooo! Non è questa..."
            )

            st.write(
                "Hai ancora **2 tentativi**."
            )

        elif tentativi == 2:

            st.warning(
                "❌ Daiii pensa bene"
            )

            st.write(
                "Hai ancora **1 tentativo**."
            )

            st.info(
                "🍦 **Nuovo indizio sbloccato: Gelato**"
            )

        if st.button(
            "➡️ Prova ancora",
            use_container_width=True
        ):

            st.session_state.giorno21_errore = False
            st.rerun()

        return


    # -------------------------
    # NUMERO TENTATIVO
    # -------------------------

    st.divider()

    st.subheader(
        f"🎯 Tentativo {tentativi + 1} di 3"
    )


    # -------------------------
    # INSERIMENTO RISPOSTA
    # -------------------------

    risposta = st.text_input(
        "🤔 Qual è la parola misteriosa?",
        max_chars=30,
        key=f"giorno21_tentativo_{tentativi}"
    )


    # -------------------------
    # CONTROLLO RISPOSTA
    # -------------------------

    if st.button(
        "🔎 Prova!",
        use_container_width=True
    ):

        risposta = risposta.strip().lower()


        # -------------------------
        # RISPOSTA VUOTA
        # -------------------------

        if not risposta:

            st.warning(
                "Scrivi prima una risposta! 😏"
            )

            return


        # -------------------------
        # RISPOSTA CORRETTA
        # -------------------------

        if risposta == "topi":

            aggiungi_punti(9, 4)

            st.session_state.giorno21_finito = True

            st.success(
                "🎉 INDOVINATO!"
            )

            st.write(
                "🏆 **Hai conquistato 4 punti!**"
            )

            st.balloons()

            return


        # -------------------------
        # RISPOSTA SBAGLIATA
        # -------------------------

        st.session_state.giorno21_tentativi += 1

        tentativi = st.session_state.giorno21_tentativi


        # -------------------------
        # TERZO ERRORE → FINE GIOCO
        # -------------------------

        if tentativi >= 3:

            # Segna il giorno come completato
            # anche se ha conquistato 0 punti
            aggiungi_punti(9, 0)

            st.session_state.giorno21_finito = True

            st.error(
                "😂 Niente da fare! Hai sbagliato tutti e 3 i tentativi."
            )

            st.write(
                "💡 La parola misteriosa era:"
            )

            st.success(
                "🍪 **topi**"
            )

            st.write(
                "🏆 **Hai conquistato 0 punti.**"
            )

            return


        # -------------------------
        # PRIMO / SECONDO ERRORE
        # -------------------------

        st.session_state.giorno21_errore = True

        st.rerun()
