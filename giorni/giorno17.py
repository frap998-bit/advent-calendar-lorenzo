
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

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
    # INIZIALIZZAZIONE
    # =====================================================

    if "giorno17_indizio" not in st.session_state:
        st.session_state.giorno17_indizio = 0

    if "giorno17_finito" not in st.session_state:
        st.session_state.giorno17_finito = False

    if "giorno17_risposta_corretta" not in st.session_state:
        st.session_state.giorno17_risposta_corretta = False

    if "giorno17_punti_ottenuti" not in st.session_state:
        st.session_state.giorno17_punti_ottenuti = 0

    indizio = st.session_state.giorno17_indizio

    # =====================================================
    # TITOLO
    # =====================================================

    st.header("Giorno 17 — DOVE, COME, QUANDO E PERCHÉ?")

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(17):

        st.success("✅ Giorno 17 completato!")

        st.write(
            f"🏆 Hai conquistato "
            f"**{st.session_state.giorno17_punti_ottenuti} punti!**"
        )

        st.write("Ecco tutti gli indizi della parola misteriosa 👀")

        for titolo, testo, punti in indizi:
            st.subheader(titolo)
            st.info(testo)

        st.divider()

        st.subheader("La parola misteriosa era...")

        st.markdown(
            """
            <h1 style="
                text-align: center;
                color: #e91e63;
                letter-spacing: 4px;
                font-weight: bold;
            ">
                CACCA 💩
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.write("❤️ Spero che adesso sia tutto più chiaro!")

        return

    # =====================================================
    # GIOCO GIÀ FINITO NELLA SESSIONE
    # =====================================================

    if st.session_state.giorno17_finito:

        st.divider()

        for titolo, testo, punti in indizi:
            st.subheader(titolo)
            st.info(testo)

        if st.session_state.giorno17_risposta_corretta:

            st.success("🎉 Esatto! La parola era **CACCA**! 💩")

            st.success(
                f"🏆 Hai conquistato "
                f"**{st.session_state.giorno17_punti_ottenuti} punti!**"
            )

        else:

            st.error("❌ Hai utilizzato tutti gli indizi!")

            st.warning("💩 **La parola era: CACCA!**")

            st.write("🏆 **Hai conquistato 0 punti.**")

        return

    # =====================================================
    # INTRODUZIONE
    # =====================================================

    st.write(
        "Ti darò **4 indizi** per aiutarti a indovinare "
        "una parola misteriosa. 👀"
    )

    st.write(
        "Prima la indovini, più punti guadagni! 🏆"
    )

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
        "Qual è la parola?",
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

        if not risposta_pulita:

            st.warning("Scrivi prima una risposta! 😏")
            return

        # -------------------------------------------------
        # RISPOSTA CORRETTA
        # -------------------------------------------------

        if risposta_pulita == "cacca":

            punti = indizi[indizio][2]

            aggiungi_punti(17, punti)

            st.session_state.giorno17_punti_ottenuti = punti
            st.session_state.giorno17_risposta_corretta = True
            st.session_state.giorno17_finito = True

            st.rerun()

        # -------------------------------------------------
        # RISPOSTA ERRATA
        # -------------------------------------------------

        else:

            if indizio == 3:

                aggiungi_punti(17, 0)

                st.session_state.giorno17_punti_ottenuti = 0
                st.session_state.giorno17_finito = True
                st.session_state.giorno17_risposta_corretta = False

                st.rerun()

            else:

                st.error(
                    "❌ Non è questa! Puoi riprovare "
                    "oppure vedere il prossimo indizio."
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
