import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(9):
        st.success("✅ Giorno 9 completato!")
        st.write("🏆 Hai già conquistato il punto di questa sfida.")
        return


    # -------------------------
    # INIZIALIZZAZIONE TENTATIVI
    # -------------------------

    if "giorno09_tentativi" not in st.session_state:
        st.session_state.giorno09_tentativi = 0


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("🔐 Giorno 9 — La parola misteriosa")

    st.write(
        "C'è una parola che ha un significato particolare per noi. ❤️"
    )

    st.write(
        "Hai **3 tentativi** per indovinarla."
    )

    st.info(
        "🎯 Se indovini la parola conquisti **1 punto**. "
        "Dopo 2 tentativi sbagliati si sbloccherà un nuovo indizio..."
    )


    # -------------------------
    # INDIZI
    # -------------------------

    st.subheader("💡 Gli indizi")

    st.write("☀️ **1. Estate**")

    st.write("😂 **2. Barzelletta**")

    st.write("🎨 **3. 3 colori**")

    if st.session_state.giorno09_tentativi >= 2:
        st.write("🍦 **4. Gelato**")
    else:
        st.write("❓ **4. -**")


    # -------------------------
    # TENTATIVI
    # -------------------------

    st.write("")

    tentativo = st.text_input(
        "🤔 Qual è la parola misteriosa?",
        max_chars=30,
        key=f"giorno09_tentativo_{st.session_state.giorno09_tentativi}"
    )


    # -------------------------
    # CONTROLLO
    # -------------------------

    if st.button(
        "🔎 Prova!",
        use_container_width=True
    ):

        risposta = tentativo.strip().lower()

        if not risposta:
            st.warning(
                "Scrivi prima una risposta! 😏"
            )

        elif risposta == "cucciolone":

            aggiungi_punti(9, 1)

            st.session_state.giorno09_tentativi = 0

            st.success(
                "🎉 INDOVINATO!"
            )

            st.write(
                "🏆 **Hai conquistato 1 punto!**"
            )

            st.balloons()

        else:

            st.session_state.giorno09_tentativi += 1

            tentativi = st.session_state.giorno09_tentativi

            if tentativi == 1:

                st.warning(
                    "❌ Nooo! Non è questa... "
                    "Hai ancora **2 tentativi**! 😏"
                )

                st.rerun()

            elif tentativi == 2:

                st.warning(
                    "❌ Ancora sbagliato! "
                    "Hai ancora **1 tentativo**!"
                )

                st.info(
                    "🍦 **Nuovo indizio sbloccato: Gelato**"
                )

                st.rerun()

            else:

                st.error(
                    "😂 Niente da fare! Hai esaurito i 3 tentativi."
                )

                st.write(
                    "💡 La parola misteriosa era:"
                )

                st.success(
                    "🍪 **CUCCIOLONE**"
                )

                st.write(
                    "🏆 **Hai conquistato 0 punti.**"
                )

                st.session_state.giorno09_tentativi = 0
