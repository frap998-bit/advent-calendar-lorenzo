
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(10):
        st.success("✅ Giorno 10 completato!")
        st.write(
            "🏆 Hai già completato questa sfida."
        )
        return


    # -------------------------
    # INIZIALIZZAZIONE
    # -------------------------

    if "giorno10_errori" not in st.session_state:
        st.session_state.giorno10_errori = 0

    if "giorno10_lettere" not in st.session_state:
        st.session_state.giorno10_lettere = []

    if "giorno10_finito" not in st.session_state:
        st.session_state.giorno10_finito = False

    if "giorno10_vinto" not in st.session_state:
        st.session_state.giorno10_vinto = False


    parola = "SPOSAMI"
    errori = st.session_state.giorno10_errori
    lettere = st.session_state.giorno10_lettere


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("💍 Giorno 10 — L'impiccato")

    st.write(
        "C'è una parola misteriosa da indovinare..."
    )

    st.write(
        "Hai a disposizione **6 errori**. "
        "Riuscirai a scoprire la parola? 👀"
    )

    st.info(
        "🎯 Se indovini la parola conquisti **4 punti**!"
    )


    # -------------------------
    # GIOCO GIÀ FINITO
    # -------------------------

    if st.session_state.giorno10_finito:

        st.divider()

        if st.session_state.giorno10_vinto:

            st.success(
                "🎉 HAI INDOVINATO!"
            )

            st.write(
                "💍 La parola era:"
            )

            st.success(
                "❤️ **SPOSAMI** ❤️"
            )

            st.write(
                "🏆 **Hai conquistato 4 punti!**"
            )

        else:

            st.error(
                "💀 Hai fatto 6 errori!"
            )

            st.write(
                "La parola era:"
            )

            st.success(
                "💍 **SPOSAMI**"
            )

            st.write(
                "🏆 **Hai conquistato 0 punti.**"
            )

        return


    # -------------------------
    # PAROLA NASCOSTA
    # -------------------------
    
    frase_visualizzata = ""
    
    for carattere in frase:
    
        if carattere == " ":
            frase_visualizzata += "&nbsp;&nbsp;&nbsp;"
    
        elif carattere in lettere:
            frase_visualizzata += carattere + " "
    
        else:
            frase_visualizzata += "_ "
    
    
    st.divider()
    
    st.subheader("🔤 La frase")
    
    st.markdown(
        f"""
        <h1 style="
            text-align: center;
            letter-spacing: 8px;
            font-weight: bold;
        ">
            {frase_visualizzata}
        </h1>
        """,
        unsafe_allow_html=True
    )


    # -------------------------
    # STATO DEL GIOCO
    # -------------------------

    st.write(
        f"❌ Errori: **{errori} / 6**"
    )

    if lettere:
        st.write(
            "🔠 Lettere già provate: "
            + ", ".join(lettere)
        )


    # -------------------------
    # CONTROLLO VITTORIA
    # -------------------------

    if all(lettera in lettere for lettera in parola):

        aggiungi_punti(10, 4)

        st.session_state.giorno10_finito = True
        st.session_state.giorno10_vinto = True

        st.success(
            "🎉 BRAVISSIMO! Hai indovinato la parola!"
        )

        st.write(
            "💍 **SPOSAMI**"
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
        key=f"giorno10_input_{errori}_{len(lettere)}"
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

        st.session_state.giorno10_lettere.append(lettera)


        # -------------------------
        # LETTERA SBAGLIATA
        # -------------------------

        if lettera not in parola:

            st.session_state.giorno10_errori += 1

            errori = st.session_state.giorno10_errori


            # -------------------------
            # SEI ERRORI → FINE
            # -------------------------

            if errori >= 6:

                aggiungi_punti(10, 0)

                st.session_state.giorno10_finito = True
                st.session_state.giorno10_vinto = False

                st.rerun()

            else:

                st.warning(
                    f"❌ Lettera sbagliata! "
                    f"Hai ancora **{6 - errori} errori**."
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
