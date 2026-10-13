
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # FRASE DA INDOVINARE
    # =====================================================

    frase = "TI AMO TANTO"

    # =====================================================
    # INIZIALIZZAZIONE
    # =====================================================

    if "giorno23_errori" not in st.session_state:
        st.session_state.giorno23_errori = 0

    if "giorno23_lettere" not in st.session_state:
        st.session_state.giorno23_lettere = []

    if "giorno23_finito" not in st.session_state:
        st.session_state.giorno23_finito = False

    if "giorno23_vinto" not in st.session_state:
        st.session_state.giorno23_vinto = False

    if "giorno23_punti_salvati" not in st.session_state:
        st.session_state.giorno23_punti_salvati = False

    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 23 — L'impiccato")

    # =====================================================
    # RISULTATO DELLA PARTITA APPENA TERMINATA
    # Deve precedere giorno_completato()
    # =====================================================

    if st.session_state.giorno23_finito:

        st.divider()

        if st.session_state.giorno23_vinto:

            st.balloons()
            st.success("🎉 HAI INDOVINATO!")

            st.write("❤️ La frase era:")

            st.markdown(
                """
                <h1 style="text-align: center; color: #e75480;">
                    ❤️ TI AMO TANTO ❤️
                </h1>
                """,
                unsafe_allow_html=True
            )

            st.write("🏆 **Hai conquistato 4 punti!**")

        else:

            st.error("💀 Hai fatto 4 errori!")

            st.write("La frase era:")

            st.markdown(
                """
                <h1 style="text-align: center; color: #e75480;">
                    ❤️ TI AMO TANTO ❤️
                </h1>
                """,
                unsafe_allow_html=True
            )

            st.write("🏆 **Hai conquistato 0 punti.**")

        return

    # =====================================================
    # CONTROLLO COMPLETAMENTO PRECEDENTE
    # =====================================================

    if giorno_completato(23):

        st.success("✅ Giorno 23 completato!")

        st.write("La frase misteriosa era...")

        st.markdown(
            """
            <div style="
                text-align: center;
                padding: 25px 10px;
                border-radius: 15px;
                background-color: rgba(255, 105, 180, 0.12);
            ">
                <div style="font-size: 42px;">❤️</div>
                <div style="
                    font-size: 32px;
                    font-weight: bold;
                    letter-spacing: 4px;
                ">TI AMO TANTO</div>
                <div style="font-size: 42px;">❤️</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("🏆 Hai già completato questa sfida.")

        return

    # =====================================================
    # ISTRUZIONI
    # =====================================================

    st.write("C'è una frase misteriosa da indovinare...")

    st.write(
        "Hai a disposizione **4 errori**. "
        "Riuscirai a scoprirla? 👀"
    )

    st.info("🎯 Se indovini la frase conquisti **4 punti!**")

    # =====================================================
    # FRASE NASCOSTA
    # =====================================================

    lettere = st.session_state.giorno23_lettere
    errori = st.session_state.giorno23_errori

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

    # =====================================================
    # STATO DEL GIOCO
    # =====================================================

    st.write(f"❌ Errori: **{errori} / 4**")

    if lettere:
        st.write(
            "🔠 Lettere già provate: "
            + ", ".join(lettere)
        )

    # =====================================================
    # CONTROLLO VITTORIA
    # =====================================================

    lettere_da_indovinare = [
        carattere
        for carattere in frase
        if carattere != " "
    ]

    if all(
        lettera in lettere
        for lettera in lettere_da_indovinare
    ):

        if not st.session_state.giorno23_punti_salvati:

            salvato = aggiungi_punti(23, 4)

            if not salvato:
                st.warning(
                    "Non è stato possibile registrare i punti. "
                    "Controlla lo stato del Giorno 23 su Supabase."
                )
                return

            st.session_state.giorno23_punti_salvati = True

        st.session_state.giorno23_finito = True
        st.session_state.giorno23_vinto = True

        st.rerun()

    # =====================================================
    # INSERIMENTO LETTERA
    # =====================================================

    st.divider()

    lettera = st.text_input(
        "✏️ Inserisci una lettera:",
        max_chars=1,
        key=f"giorno23_input_{errori}_{len(lettere)}"
    )

    # =====================================================
    # PULSANTE
    # =====================================================

    if st.button("🔎 Prova!", use_container_width=True):

        lettera = lettera.strip().upper()

        if not lettera:
            st.warning("Scrivi una lettera! 😏")
            return

        if not lettera.isalpha():
            st.warning("Inserisci una lettera valida! 😏")
            return

        if lettera in lettere:
            st.warning("Questa lettera l'hai già provata! 👀")
            return

        st.session_state.giorno23_lettere.append(lettera)

        # -------------------------------------------------
        # LETTERA SBAGLIATA
        # -------------------------------------------------

        if lettera not in frase.replace(" ", ""):

            st.session_state.giorno23_errori += 1

            if st.session_state.giorno23_errori >= 4:

                salvato = aggiungi_punti(23, 0)

                if not salvato:
                    st.warning(
                        "Non è stato possibile registrare "
                        "la conclusione della sfida su Supabase."
                    )
                    return

                st.session_state.giorno23_finito = True
                st.session_state.giorno23_vinto = False

        # Il rerun mostra il risultato prima del controllo
        # di completamento persistente.
        st.rerun()

