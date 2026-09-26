import streamlit as st
import random

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(4):
        st.success("✅ Giorno 4 completato!")
        st.write("🏆 Hai già conquistato i punti di questa sfida.")
        return


    # =====================================================
    # ORDINE CORRETTO
    # =====================================================

    ordine_corretto = [
        "🏐 Beach volley",
        "📺 Guardare serie TV",
        "🎹 Suonare",
        "📖 Leggere"
    ]


    # =====================================================
    # INIZIALIZZAZIONE ORDINE
    # =====================================================

    if "giorno04_ordine" not in st.session_state:

        st.session_state.giorno04_ordine = ordine_corretto.copy()

        random.shuffle(
            st.session_state.giorno04_ordine
        )


    # =====================================================
    # INIZIALIZZAZIONE TENTATIVI
    # =====================================================

    if "giorno04_tentativi" not in st.session_state:
        st.session_state.giorno04_tentativi = 0


    ordine = st.session_state.giorno04_ordine

    tentativi = st.session_state.giorno04_tentativi

    tentativi_rimasti = 3 - tentativi


    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 4 — Quanto conosci Francesca?")

    st.write(
        "Vediamo se riesci a capire quanto bene conosci "
        "i miei gusti... 👀"
    )

    st.write(
        "Metti in ordine queste attività dalla "
        "**mia preferita alla meno preferita**."
    )

    st.info(
        f"🎯 Hai a disposizione **3 tentativi**. "
        f"Te ne rimangono **{tentativi_rimasti}**."
    )


    # =====================================================
    # ORDINE ATTUALE
    # =====================================================

    st.subheader("📋 Il tuo ordine")

    st.caption(
        "Usa ⬆️ e ⬇️ per spostare le attività."
    )


    # =====================================================
    # ELENCO ATTIVITÀ
    # =====================================================

    for i in range(len(ordine)):

        col_numero, col_attivita, col_su, col_giu = st.columns(
            [0.7, 4.5, 0.8, 0.8]
        )



        # -------------------------------------------------
        # NUMERO
        # -------------------------------------------------

        with col_numero:

            st.write(
                f"**{i + 1}.**"
            )


        # -------------------------------------------------
        # ATTIVITÀ
        # -------------------------------------------------

        with col_attivita:

            st.write(
                ordine[i]
            )


        # -------------------------------------------------
        # FRECCIA SU
        # -------------------------------------------------

        with col_su:

            if st.button(
                "⬆️",
                key=f"giorno04_up_{i}",
                disabled=(i == 0)
            ):

                ordine[i - 1], ordine[i] = (
                    ordine[i],
                    ordine[i - 1]
                )

                st.session_state.giorno04_ordine = ordine

                st.rerun()


        # -------------------------------------------------
        # FRECCIA GIÙ
        # -------------------------------------------------

        with col_giu:

            if st.button(
                "⬇️",
                key=f"giorno04_down_{i}",
                disabled=(i == len(ordine) - 1)
            ):

                ordine[i], ordine[i + 1] = (
                    ordine[i + 1],
                    ordine[i]
                )

                st.session_state.giorno04_ordine = ordine

                st.rerun()


    # =====================================================
    # CONTROLLO ORDINE
    # =====================================================

    st.write("")

    if st.button(
        "💘 Controlla il mio ordine",
        use_container_width=True
    ):

        # -------------------------------------------------
        # AUMENTA NUMERO TENTATIVI
        # -------------------------------------------------

        st.session_state.giorno04_tentativi += 1

        tentativo_corrente = (
            st.session_state.giorno04_tentativi
        )


        # -------------------------------------------------
        # CALCOLO POSIZIONI CORRETTE
        # -------------------------------------------------

        posizioni_corrette = sum(
            ordine[i] == ordine_corretto[i]
            for i in range(len(ordine))
        )


        st.divider()


        # =================================================
        # CASO 1 — TUTTO CORRETTO
        # =================================================

        if posizioni_corrette == len(ordine):

            punti_assegnati = aggiungi_punti(
                4,
                6
            )

            st.success(
                "🎉 PERFETTO! Hai indovinato tutto! ❤️"
            )

            st.balloons()

            if punti_assegnati:

                st.write(
                    "🏆 **Hai conquistato 6 punti!**"
                )

            return


        # =================================================
        # CASO 2 — TERZO TENTATIVO
        # =================================================

        if tentativo_corrente >= 3:

            punti_assegnati = aggiungi_punti(
                4,
                posizioni_corrette
            )


            if posizioni_corrette == 0:

                st.warning(
                    "😏 Tentativi terminati! "
                    "Questa volta non hai azzeccato nessuna posizione."
                )

            else:

                st.warning(
                    f"😏 Tentativi terminati! "
                    f"Hai messo **{posizioni_corrette} attività "
                    f"su 6 nella posizione corretta**."
                )


            if punti_assegnati:

                st.write(
                    f"🏆 **Hai conquistato "
                    f"{posizioni_corrette} punti!**"
                )


            # -------------------------------------------------
            # SOLUZIONE
            # -------------------------------------------------

            st.divider()

            st.subheader(
                "💡 Ecco il mio vero ordine"
            )

            for i, attivita in enumerate(
                ordine_corretto,
                start=1
            ):

                st.write(
                    f"**{i}. {attivita}**"
                )

            return


        # =================================================
        # CASO 3 — PRIMO / SECONDO TENTATIVO
        # =================================================

        st.warning(
            f"🤔 Hai **{posizioni_corrette} su 4** "
            f"attività nella posizione corretta!"
        )


        tentativi_rimasti = 3 - tentativo_corrente


        if tentativi_rimasti == 1:

            messaggio = (
                "⚠️ Ti rimane **1 solo tentativo**! "
                "Puoi ancora modificare l'ordine e riprovare."
            )

        else:

            messaggio = (
                f"💡 Hai ancora **{tentativi_rimasti} tentativi**. "
                "Puoi modificare l'ordine e riprovare!"
            )


        st.info(messaggio)
