import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(22):
        st.success("✅ Giorno 22 completato!")
        st.write("🏆 Hai già conquistato i punti di questa sfida.")
        return


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("📸 Giorno 22 — Indovina il mese!")

    st.write(
        "Riconosci queste foto e prova a ricordare "
        "quando sono state scattate. ❤️"
    )

    st.info(
        "🎯 Hai un solo tentativo. "
        "Ogni risposta corretta vale 1 punto, "
        "per un massimo di 4 punti!"
    )


    # -------------------------
    # DOMANDE
    # -------------------------

    domande = [
        {
            "foto": "immagini/Marzo 2025.png",
            "domanda": "📅 In che mese e anno è stata scattata?",
            "opzioni": [
                "Marzo 2025",
                "Aprile 2025",
                "Marzo 2026",
                "Febbraio 2025"
            ],
            "corretta": "Marzo 2025"
        },
        {
            "foto": "immagini/Aprile 2025.png",
            "domanda": "📅 In che mese e anno è stata scattata?",
            "opzioni": [
                "Marzo 2025",
                "Aprile 2025",
                "Maggio 2025",
                "Aprile 2026"
            ],
            "corretta": "Aprile 2025"
        },
        {
            "foto": "immagini/Agosto 2026.png",
            "domanda": "📅 In che mese e anno è stata scattata?",
            "opzioni": [
                "Agosto 2025",
                "Luglio 2026",
                "Agosto 2026",
                "Settembre 2026"
            ],
            "corretta": "Agosto 2026"
        },
        {
            "foto": "immagini/Novembre 2024.png",
            "domanda": "📅 In che mese e anno è stata scattata?",
            "opzioni": [
                "Ottobre 2024",
                "Novembre 2024",
                "Dicembre 2024",
                "Novembre 2025"
            ],
            "corretta": "Novembre 2024"
        }
    ]


    # -------------------------
    # RISPOSTE
    # -------------------------

    risposte = []


    # -------------------------
    # FOTO E RISPOSTE
    # -------------------------

    for i, domanda in enumerate(domande, start=1):

        st.write("")

        st.subheader(
            f"{i}. {domanda['domanda']}"
        )

        st.image(
            domanda["foto"],
            use_container_width=True
        )

        risposta = st.radio(
            "Scegli una risposta:",
            domanda["opzioni"],
            key=f"giorno22_domanda{i}"
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

        completato = aggiungi_punti(
            22,
            risposte_corrette
        )


        # -------------------------
        # RISULTATO
        # -------------------------

        st.divider()

        if risposte_corrette == 4:

            st.success(
                "🎉 PERFETTO! Hai riconosciuto tutti i mesi!"
            )

            st.balloons()

        elif risposte_corrette == 3:

            st.success(
                "🥰 Brava memoria! Ne hai riconosciute 3 su 4!"
            )

        elif risposte_corrette == 2:

            st.warning(
                "😏 Due su quattro! Non male..."
            )

        elif risposte_corrette == 1:

            st.warning(
                "😂 Una sola corretta! Puoi fare meglio..."
            )

        else:

            st.error(
                "😂 Nessuna corretta! La memoria oggi non collabora..."
            )


        st.write(
            f"🏆 **Hai conquistato {risposte_corrette} punti!**"
        )


        # -------------------------
        # RISPOSTE CORRETTE
        # -------------------------

        if risposte_corrette < 4:

            st.write("")

            st.subheader(
                "📅 Le risposte corrette erano:"
            )

            for i, domanda in enumerate(domande, start=1):

                if risposte[i - 1] != domanda["corretta"]:

                    st.write(
                        f"**{i}.** {domanda['corretta']} ✅"
                    )
