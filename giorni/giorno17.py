import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(17):
        st.success("✅ Giorno 17 completato!")
        st.write("🏆 Hai già conquistato i punti di questa sfida.")
        return


    # =====================================================
    # INIZIALIZZAZIONE
    # =====================================================

    if "giorno17_indizio" not in st.session_state:
        st.session_state.giorno17_indizio = 0

    if "giorno17_finito" not in st.session_state:
        st.session_state.giorno17_finito = False

    if "giorno17_risposta_corretta" not in st.session_state:
        st.session_state.giorno17_risposta_corretta = False


    indizio = st.session_state.giorno17_indizio


    # =====================================================
    # TITOLO
    # =====================================================

    st.header(
        "Giorno 17 — DOVE, COME, QUANDO E PERCHÉ?"
    )

    st.write(
        "Ti darò **4 indizi** per aiutarti a indovinare "
        "una parola misteriosa. 👀"
    )

    st.write(
        "Più presto la indovini, più punti guadagni! 🏆"
    )


    # =====================================================
    # INDIZI
    # =====================================================

    indizi = [
        ("📍 DOVE", "In mezzo all’erba", 4),
        ("🧩 COME", "Con tanto sforzo", 3),
        ("📅 QUANDO", "Durante un giretto", 2),
        (
            "❤️ PERCHÉ",
            "Perché quando raccogli quella di Olmo con il sacchetto, io corro via finché non la butti…",
            1
        )
    ]


    # =====================================================
    # SE HA INDOVINATO
    # MOSTRA TUTTI GLI INDIZI
    # =====================================================

    if st.session_state.giorno17_risposta_corretta:

        for titolo, testo, punti in indizi:

            st.subheader(titolo)

            st.info(testo)


        st.success(
            "🎉 Esatto! La parola era **CACCA**! 💩"
        )

        st.balloons()

        return


    # =====================================================
    # MOSTRA GLI INDIZI SBLOCCATI
    # =====================================================

    for i in range(indizio + 1):

        titolo, testo, punti = indizi[i]

        st.subheader(titolo)

        st.info(testo)

        st.caption(
            f"🏆 Se indovini ora: **{punti} punti**"
        )


    # =====================================================
    # RISPOSTA
    # =====================================================

    st.write("")

    risposta = st.text_input(
        "💩 Qual è la parola?",
        key="giorno17_risposta"
    )


    # =====================================================
    # CONTROLLO RISPOSTA
    # =====================================================

    if st.button(
        "💘 Indovina!",
        use_container_width=True
    ):

        risposta_pulita = risposta.strip().lower()


        # -------------------------------------------------
        # RISPOSTA CORRETTA
        # -------------------------------------------------

        if risposta_pulita == "cacca":

            punti = indizi[indizio][2]

            punti_assegnati = aggiungi_punti(
                17,
                punti
            )

            st.session_state.giorno17_risposta_corretta = True
            st.session_state.giorno17_finito = True

            st.rerun()


        # -------------------------------------------------
        # RISPOSTA ERRATA
        # -------------------------------------------------

        else:

            if indizio == 3:

                # Mostra comunque tutti gli indizi

                for titolo, testo, punti in indizi:

                    st.subheader(titolo)

                    st.info(testo)


                st.error(
                    "❌ Peccato! Hai utilizzato tutti gli indizi."
                )

                st.warning(
                    "💩 **La parola era: CACCA!**"
                )

                st.write(
                    "Questa volta niente punti 😜"
                )

                st.session_state.giorno17_finito = True

                return

            else:

                st.error(
                    "❌ Non è questa! "
                    "Puoi riprovare oppure vedere il prossimo indizio."
                )


    # =====================================================
    # PROSSIMO INDIZIO
    # =====================================================

    if indizio < 3:

        st.write("")

        if st.button(
            "🔎 Mostra prossimo indizio",
            use_container_width=True
        ):

            st.session_state.giorno17_indizio += 1

            st.rerun()


    # =====================================================
    # ULTIMO INDIZIO
    # =====================================================

    else:

        st.divider()

        st.write(
            "❤️ Questo è l'ultimo indizio. "
            "Ora devi aver capito!"
        )
