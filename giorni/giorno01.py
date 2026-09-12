import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(1):
        st.success("✅ Giorno 1 completato!")
        st.write("🏆 Hai già conquistato i 5 punti di questa sfida.")
        return


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("❤️ Giorno 1 — Chi dei due?")

    st.write(
        "Per ogni domanda scegli chi dei due pensi sia la risposta corretta."
    )

    st.info(
        "🎯 Devi indovinare tutte e 5 le risposte per conquistare i 5 punti! Ovviamente ho scelto io quale sia la risposta corretta, quindi per reclami o polemiche, rivolgersi non a me."
    )


    # -------------------------
    # DOMANDE
    # -------------------------

    domande = [
        {
            "domanda": "Chi dei due è più dolce?",
            "risposta": "Lorenzo"
        },
        {
            "domanda": "Chi dei due è più ritardatario?",
            "risposta": "Francesca"
        },
        {
            "domanda": "Chi dei due è più competitivo?",
            "risposta": "Francesca"
        },
        {
            "domanda": "Chi dei due è più disordinato?",
            "risposta": "Lorenzo"
        },

        {
            "domanda": "Chi dei due è più geloso?",
            "risposta": "Lorenzo"
        }
    ]


    risposte = []


    # -------------------------
    # RISPOSTE
    # -------------------------

    for i, domanda in enumerate(domande, start=1):

        st.write("")
        st.subheader(f"{i}. {domanda['domanda']}")

        risposta = st.radio(
            "Scegli:",
            ["Francesca", "Lorenzo"],
            key=f"giorno1_domanda{i}",
            horizontal=True
        )

        risposte.append(risposta)


    st.write("")


    # -------------------------
    # CONTROLLO
    # -------------------------

    if st.button(
        "💘 Controlla le risposte",
        use_container_width=True
    ):

        risposte_corrette = 0

        for i, domanda in enumerate(domande):
            if risposte[i] == domanda["risposta"]:
                risposte_corrette += 1


        # -------------------------
        # TUTTE CORRETTE
        # -------------------------

        if risposte_corrette == 5:

            punti_assegnati = aggiungi_punti(1, 5)

            st.success(
                "🎉 PERFETTO! Le hai azzeccate tutte!"
            )

            st.balloons()

            if punti_assegnati:
                st.write(
                    "🏆 **Hai conquistato 5 punti!**"
                )
            else:
                st.info(
                    "I 5 punti di questo gioco sono già stati assegnati 😉"
                )


        # -------------------------
        # NON TUTTE CORRETTE
        # -------------------------

        else:

            st.error(
                f"❌ Ne hai indovinate {risposte_corrette} su 5."
            )

            st.warning(
                "Niente punti questa volta 😈 "
                "Riprova e cerca di conoscerci meglio!"
            )
