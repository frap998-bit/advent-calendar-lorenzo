
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(23):
        st.success("✅ Giorno 23 completato!")
        st.write(
            "🏆 Hai già completato questa sfida."
        )
        return


    # -------------------------
    # INIZIALIZZAZIONE
    # -------------------------

    if "giorno23_errori" not in st.session_state:
        st.session_state.giorno23_errori = 0

    if "giorno23_lettere" not in st.session_state:
        st.session_state.giorno23_lettere = []

    if "giorno23_finito" not in st.session_state:
        st.session_state.giorno23_finito = False

    if "giorno23_vinto" not in st.session_state:
        st.session_state.giorno23_vinto = False


    frase = "TI AMO TANTO"
    errori = st.session_state.giorno23_errori
    lettere = st.session_state.giorno23_lettere


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("❤️ Giorno 23 — L'impiccato")

    st.write(
        "C'è una frase misteriosa da indovinare..."
    )

    st.write(
        "Hai a disposizione **7 errori**. "
        "Riuscirai a scoprirla? 👀"
    )

    st.info(
        "🎯 Se indovini la frase conquisti **4 punti!**"
    )


    # -------------------------
    # GIOCO GIÀ FINITO
    # -------------------------

    if st.session_state.giorno23_finito:

        st.divider()

        if st.session_state.giorno23_vinto:

            st.success(
                "🎉 HAI INDOVINATO!"
            )

            st.write(
                "❤️ La frase era:"
            )

            st.success(
                "❤️ **TI AMO TANTO** ❤️"
            )

            st.write(
                "🏆 **Hai conquistato 4 punti!**"
            )

        else:

            st.error(
                "💀 Hai fatto 7 errori!"
            )

            st.write(
                "La frase era:"
            )

            st.success(
                "❤️ **TI AMO TANTO**"
            )

            st.write(
                "🏆 **Hai conquistato 0 punti.**"
            )

        return


    # -------------------------
    # FRASE NASCOSTA
    # -------------------------

    frase_visualizzata = ""

    for carattere in frase:

        if carattere == " ":
            frase_visualizzata += "&nbsp;&nbsp;&nbsp;"

        elif carattere in lettere:
            frase_visualizzata += f"{carattere} "

        else:
            frase_visualizzata += "_ "


    st.divider()

    st.subheader("🔤 La frase")

    st.markdown(
        f"<h1 style='text-align: center; letter-spacing: 8px;'>"
        f"{frase_visualizzata}"
        f"</h1>",
        unsafe_allow_html=True
    )


    # -------------------------
    # STATO DEL GIOCO
    # -------------------------

    st.write(
        f"❌ Errori: **{errori} / 7**"
    )

    if lettere:
        st.write(
            "🔠 Lettere già provate: "
            + ", ".join(lettere)
        )


    # -------------------------
    # CONTROLLO VITTORIA
    # -------------------------

    lettere_da_indovinare = [
        carattere
        for carattere in frase
        if carattere != " "
    ]

    if all(lettera in lettere for lettera in lettere_da_indovinare):

        aggiungi_punti(23, 4)

        st.session_state.giorno23_finito = True
        st.session_state.giorno23_vinto = True

        st.success(
            "🎉 BRAVISSIMO! Hai indovinato la frase!"
        )

        st.write(
            "❤️ **TI AMO TANTO** ❤️"
        )

        st.write(
            "🏆 **Hai conquistato 4 punti!**"
        )

        st.balloons()

        return


    # -------------------------
    # INSERIMENTO LETTERA
    # -------------------------

    st.divider()

    lettera = st.text_input(
        "✏️ Inserisci una lettera:",
        max_chars=1,
        key=f"giorno23_input_{errori}_{len(lettere)}"
    )


    # -------------------------
    # PULSANTE
    # -------------------------

    if st.button(
        "🔎 Prova!",
        use_container_width=True
    ):

        lettera = lettera.strip().upper()


        # -------------------------
        # INPUT VUOTO
        # -------------------------

        if not lettera:

            st.warning(
                "Scrivi una lettera! 😏"
            )

            return


        # -------------------------
        # CONTROLLO LETTERA
        # -------------------------

        if not lettera.isalpha():

            st.warning(
                "Inserisci una lettera valida! 😏"
            )

            return


        # -------------------------
        # LETTERA GIÀ PROVATA
        # -------------------------

        if lettera in lettere:

            st.warning(
                "Questa lettera l'hai già provata! 👀"
            )

            return


        # -------------------------
        # AGGIUNGI LETTERA
        # -------------------------

        st.session_state.giorno23_lettere.append(lettera)


        # -------------------------
        # LETTERA SBAGLIATA
        # -------------------------

        if lettera not in frase.replace(" ", ""):

            st.session_state.giorno23_errori += 1

            errori = st.session_state.giorno23_errori


            # -------------------------
            # 7 ERRORI → FINE
            # -------------------------

            if errori >= 7:

                aggiungi_punti(23, 0)

                st.session_state.giorno23_finito = True
                st.session_state.giorno23_vinto = False

                st.rerun()

            else:

                st.warning(
                    f"❌ Lettera sbagliata! "
                    f"Hai ancora **{7 - errori} errori**."
                )

                st.rerun()


        # -------------------------
        # LETTERA CORRETTA
        # -------------------------

        else:

            st.success(
                f"✅ La lettera **{lettera}** c'è!"
            )

            st.rerun()
