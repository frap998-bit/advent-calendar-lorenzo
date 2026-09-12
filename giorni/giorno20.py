import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(20):
        st.success("✅ Giorno 20 completato!")
        st.write("🏆 Hai già conquistato i 5 punti di questa sfida.")
        return


    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 20 — Quanto ti ricordi?")

    st.write(
        "Vediamo quanto ti ricordi delle nostre piccole abitudini... 👀"
    )

    st.write(
        "Rispondi alle domande e prova a indovinare tutte le parole!"
    )


    # =====================================================
    # DOMANDE
    # =====================================================

    domande = [
        {
            "numero": 1,
            "domanda": "Come è detto anche il Prof. Omar?",
            "lettere": 8,
            "soluzione": "SCHETTINI"
        },
        {
            "numero": 2,
            "domanda": "Qual è il nostro posto più gettonato per una cena?",
            "lettere": 3,
            "soluzione": "AMO"
        },
        {
            "numero": 3,
            "domanda": "Cosa ti ha fatto acquisire il potere di Maranza?",
            "lettere": 7,
            "soluzione": "CANOTTA"
        },
        {
            "numero": 4,
            "domanda": "Il nostro motto? (Sono due parole)",
            "lettere": 12,
            "soluzione": "PIANO PIANO"
        }
    ]


    # =====================================================
    # INPUT RISPOSTE
    # =====================================================

    risposte = {}


    for domanda in domande:

        numero = domanda["numero"]
        testo = domanda["domanda"]
        numero_lettere = domanda["lettere"]


        # -------------------------------------------------
        # DOMANDA
        # -------------------------------------------------

        st.markdown(
            f"### {numero}. {testo}"
        )

        st.caption(
            f"🔤 {numero_lettere} lettere"
        )


        # -------------------------------------------------
        # INPUT
        # -------------------------------------------------

        risposte[numero] = st.text_input(
            f"Risposta {numero}",
            max_chars=numero_lettere,
            key=f"giorno20_risposta_{numero}",
            placeholder="Scrivi qui la risposta..."
        )


        st.write("")


    # =====================================================
    # CONTROLLO
    # =====================================================

    if st.button(
        "🔎 Controlla risposte",
        use_container_width=True
    ):

        risposte_corrette = 0

        for domanda in domande:

            numero = domanda["numero"]

            soluzione = domanda["soluzione"]

            risposta = (
                risposte[numero]
                .strip()
                .upper()
                .replace(" ", "")
            )


            if risposta == soluzione:

                risposte_corrette += 1


        # =================================================
        # TUTTO CORRETTO
        # =================================================

        if risposte_corrette == len(domande):

            punti_assegnati = aggiungi_punti(20, 5)

            st.success(
                "🎉 PERFETTO! Hai indovinato tutte le risposte! ❤️"
            )

            st.balloons()

            if punti_assegnati:

                st.write(
                    "🏆 **Hai conquistato 5 punti!**"
                )


        # =================================================
        # RISPOSTE PARZIALMENTE CORRETTE
        # =================================================

        else:

            st.warning(
                f"Ci sei quasi! Hai indovinato "
                f"**{risposte_corrette} su {len(domande)}**. 😉"
            )

            st.info(
                "💡 Controlla bene le risposte e riprova!"
            )
