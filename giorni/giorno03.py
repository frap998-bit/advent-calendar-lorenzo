
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(3):
        st.success("✅ Giorno 3 completato!")
        st.write("🏆 Hai già conquistato i 5 punti di questa sfida.")
        return


    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 3 — Quanto ti ricordi?")

    st.write(
        "Vediamo quanto ti ricordi delle nostre piccole avventure... 👀"
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
            "domanda": 'Non sopporto quando mi dici che "parto in ____".',
            "lettere": 6,
            "soluzione": "QUARTA"
        },
        {
            "numero": 2,
            "domanda": "La cosa che mia mamma ci ha ordinato di sistemare quest’estate.",
            "lettere": 8,
            "soluzione": "ALTALENA"
        },
        {
            "numero": 3,
            "domanda": "Posto dove ho patito il freddo, perché tu invece stavi bene.",
            "lettere": 7,
            "soluzione": "LIVIGNO"
        },
        {
            "numero": 4,
            "domanda": "Il 2 che ci ha fatto conoscere.",
            "lettere": 4,
            "soluzione": "LUCA"
        },
        {
            "numero": 5,
            "domanda": "Una volta sei rimasto con lei a terra.",
            "lettere": 5,
            "soluzione": "GOMMA"
        },
        {
            "numero": 6,
            "domanda": "L'allergia mi impedisce di diventarlo.",
            "lettere": 7,
            "soluzione": "GATTARA"
        },
        {
            "numero": 7,
            "domanda": "L'asino che non è un asino.",
            "lettere": 4,
            "soluzione": "OLMO"
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
            key=f"giorno03_risposta_{numero}",
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
            )


            if risposta == soluzione:

                risposte_corrette += 1


        # =================================================
        # TUTTO CORRETTO
        # =================================================

        if risposte_corrette == len(domande):

            punti_assegnati = aggiungi_punti(3, 5)

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
