import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(2):
        st.success("✅ Giorno 2 completato!")
        st.write("🏆 Hai già conquistato i punti di questa sfida.")
        return


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("📚 Giorno 2 — Quanto mi conosci?")

    st.write(
        "Vediamo quanto conosci la tua dolce metà... 👀❤️"
    )

    st.write(
        "Rispondi alle 5 domande. "
        "Per ogni risposta corretta conquisti **1 punto**!"
    )


    # -------------------------
    # DOMANDE
    # -------------------------

    domande = [
        {
            "domanda": "📖 Quale libro sto leggendo in questo momento?",
            "opzioni": [
                "Il nome della rosa — Umberto Eco",
                "La gatta persiana — Alessandro Varaldo",
                "Dieci piccoli indiani — Agatha Christie",
                "Il grande Gatsby — F. Scott Fitzgerald"
            ],
            "corretta": "La gatta persiana — Alessandro Varaldo"
        },

        {
            "domanda": "🎹 Quale canzone mi piace particolarmente suonare al pianoforte?",
            "opzioni": [
                "Nuvole Bianche — Ludovico Einaudi",
                "Aria — Giovanni Allevi",
                "River Flows in You — Yiruma",
                "Comptine d’un autre été — Yann Tiersen"
            ],
            "corretta": "Aria — Giovanni Allevi"
        },

        {
            "domanda": "📏 Quanto sono alta?",
            "opzioni": [
                "1,59 m",
                "1,61 m",
                "1,62 m",
                "1,63 m"
            ],
            "corretta": "1,61 m"
        },

        {
            "domanda": "💇‍♀️ Di che colore sono i miei capelli?",
            "opzioni": [
                "Biondo miele",
                "Biondo cenere",
                "Castano chiaro",
                "Biondo dorato"
            ],
            "corretta": "Biondo cenere"
        },

        {
            "domanda": "🩸 Quanti anni avevo quando mi è arrivato il ciclo per la prima volta?",
            "opzioni": [
                "12 anni",
                "13 anni",
                "14 anni",
                "15 anni"
            ],
            "corretta": "14 anni"
        }
    ]


    # -------------------------
    # RISPOSTE
    # -------------------------

    risposte = []

    for i, domanda in enumerate(domande, start=1):

        st.write("")

        st.subheader(
            f"{i}. {domanda['domanda']}"
        )

        risposta = st.radio(
            "Scegli una risposta:",
            domanda["opzioni"],
            key=f"giorno02_domanda{i}"
        )

        risposte.append(risposta)


    st.write("")


    # -------------------------
    # CONTROLLO
    # -------------------------

    if st.button(
        "🔎 Controlla le risposte",
        use_container_width=True
    ):

        risposte_corrette = 0

        for i, domanda in enumerate(domande):

            if risposte[i] == domanda["corretta"]:
                risposte_corrette += 1


        # -------------------------
        # ASSEGNAZIONE PUNTI
        # -------------------------

        punti_assegnati = aggiungi_punti(
            2,
            risposte_corrette
        )


        # -------------------------
        # RISULTATO
        # -------------------------

        st.divider()

        if risposte_corrette == 5:

            st.success(
                "🎉 PERFETTO! Mi conosci proprio benissimo!"
            )

            st.balloons()

        elif risposte_corrette >= 3:

            st.success(
                f"🥰 Niente male! Hai totalizzato "
                f"**{risposte_corrette}/5 punti!**"
            )

        elif risposte_corrette >= 1:

            st.warning(
                f"😏 Puoi fare di meglio! Hai totalizzato "
                f"**{risposte_corrette}/5 punti.**"
            )

        else:

            st.error(
                "😂 0/5... Forse dobbiamo ripassare un po'!"
            )


        if punti_assegnati:

            st.write(
                f"🏆 **Hai conquistato {risposte_corrette} punti!**"
            )


        # -------------------------
        # SOLUZIONI
        # -------------------------

        st.write("")
        st.write("### 💡 Le risposte corrette erano:")

        for i, domanda in enumerate(domande, start=1):

            st.write(
                f"**{i}.** {domanda['corretta']}"
            )
