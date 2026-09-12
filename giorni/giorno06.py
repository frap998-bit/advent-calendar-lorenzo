import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(6):
        st.success("✅ Giorno 6 completato!")
        st.write("🏆 Hai già conquistato i punti di questa sfida.")
        return


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("📸 Giorno 6 — Indovina il posto")

    st.write(
        "Vediamo quanto sei bravo a riconoscere i posti "
        "dove siamo stati insieme! ❤️"
    )

    st.info(
        "🎯 Ogni risposta corretta vale 1 punto. "
        "Puoi conquistare fino a 3 punti!"
    )


    # -------------------------
    # DOMANDE
    # -------------------------

    domande = [
        {
            "foto": "immagini/Livigno.jpeg",
            "domanda": "📍 Dove siamo?",
            "opzioni": [
                "Livigno",
                "Numana",
                "Sanremo",
                "Tortoreto"
            ],
            "corretta": "Livigno"
        },
        {
            "foto": "immagini/Numana.jpeg",
            "domanda": "📍 Dove siamo?",
            "opzioni": [
                "Sanremo",
                "Numana",
                "Livigno",
                "Seregno"
            ],
            "corretta": "Numana"
        },
        {
            "foto": "immagini/Sanremo.jpeg",
            "domanda": "📍 Dove siamo?",
            "opzioni": [
                "Tortoreto",
                "Livigno",
                "Sanremo",
                "Numana"
            ],
            "corretta": "Sanremo"
        }
    ]


    risposte = []


    # -------------------------
    # FOTO E RISPOSTE
    # -------------------------

    for i, domanda in enumerate(domande, start=1):

        st.write("")

        st.subheader(f"{i}. {domanda['domanda']}")

        st.image(
            domanda["foto"],
            use_container_width=True
        )

        risposta = st.radio(
            "Scegli una risposta:",
            domanda["opzioni"],
            key=f"giorno06_domanda{i}"
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
            6,
            risposte_corrette
        )


        # -------------------------
        # RISULTATO
        # -------------------------

        st.divider()

        if risposte_corrette == 3:

            st.success(
                "🎉 PERFETTO! Le hai riconosciute tutte!"
            )

            st.balloons()

        elif risposte_corrette == 2:

            st.success(
                "🥰 Quasi! Ne hai riconosciute 2 su 3!"
            )

        elif risposte_corrette == 1:

            st.warning(
                "😏 Una l'hai riconosciuta! Puoi fare meglio..."
            )

        else:

            st.error(
                "😂 Nessuna corretta! Mi sa che dobbiamo "
                "rifare un po' di viaggi..."
            )


        st.write(
            f"🏆 **Hai conquistato {risposte_corrette} punti!**"
        )
