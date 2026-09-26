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


    indizio = st.session_state.giorno17_indizio


    # =====================================================
    # TITOLO
    # =====================================================

    st.header("💩 Giorno 17 — Indovina la parola!")

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
    # INDIZIO CORRENTE
    # =====================================================

    titolo, testo, punti = indizi[indizio]

    st.subheader(titolo)

    st.info(testo)

    st.caption(
        f"🏆 Se indovini ora: **{punti} punti**"
    )


    # =====================================================
    # RISPOSTA
    # =====================================================

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

            punti_assegnati = aggiungi_punti(
                17,
                punti
            )

            st.success(
                "🎉 Esatto! La parola era **CACCA**! 💩"
            )

            st.balloons()

            if punti_assegnati:
                st.write(
                    f"🏆 Hai conquistato **{punti} punti!**"
                )

            st.session_state.giorno17_finito = True

            return


        # -------------------------------------------------
        # RISPOSTA ERRATA
        # -------------------------------------------------

        else:

            if indizio == 3:

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
