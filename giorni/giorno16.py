
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

    if giorno_completato(16):
        st.success("✅ Giorno 16 completato!")
        st.write(
            "🏆 Hai già conquistato i punti di questa sfida."
        )
        return


    # =====================================================
    # ORDINE CHE FRANCESCA PENSA SIA IL SUO
    # =====================================================

    ordine_corretto = [
        "🍳 Cucinare",
        "🥾 Gite in montagna",
        "🏐 Beach volley",
        "📺 Serie TV",
        "🏃 Corsa"
    ]


    # =====================================================
    # INIZIALIZZAZIONE ORDINE
    # =====================================================

    if "giorno16_ordine" not in st.session_state:

        st.session_state.giorno16_ordine = (
            ordine_corretto.copy()
        )

        random.shuffle(
            st.session_state.giorno16_ordine
        )


    ordine = st.session_state.giorno16_ordine


    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 16 — Quanto ti conosco io Francesca?")

    st.write(
        "Vediamo quanto bene conosco i tuoi gusti... 👀"
    )

    st.write(
        "Io ho fatto il mio pronostico: ora tocca a te "
        "mettere in ordine queste attività dalla "
        "**tua preferita alla meno preferita**."
    )

    st.info(
        "🎯 Per ogni posizione in cui il tuo ordine "
        "**NON coincide con il mio pronostico**, "
        "conquisti **1 punto**, perchè vuol dire che sono stata scarsa io :("
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


        with col_numero:

            st.write(
                f"**{i + 1}.**"
            )


        with col_attivita:

            st.write(
                ordine[i]
            )


        with col_su:

            if st.button(
                "⬆️",
                key=f"giorno16_up_{i}",
                disabled=(i == 0)
            ):

                ordine[i - 1], ordine[i] = (
                    ordine[i],
                    ordine[i - 1]
                )

                st.session_state.giorno16_ordine = ordine

                st.rerun()


        with col_giu:

            if st.button(
                "⬇️",
                key=f"giorno16_down_{i}",
                disabled=(i == len(ordine) - 1)
            ):

                ordine[i], ordine[i + 1] = (
                    ordine[i + 1],
                    ordine[i]
                )

                st.session_state.giorno16_ordine = ordine

                st.rerun()


    # =====================================================
    # CONTROLLO ORDINE
    # =====================================================

    st.write("")

    if st.button(
        "💘 Questo è il mio ordine!",
        use_container_width=True
    ):

        # -------------------------------------------------
        # CALCOLO POSIZIONI
        # -------------------------------------------------

        posizioni_corrette = sum(
            ordine[i] == ordine_corretto[i]
            for i in range(len(ordine))
        )

        posizioni_sbagliate = (
            len(ordine) - posizioni_corrette
        )


        # -------------------------------------------------
        # PUNTI
        # -------------------------------------------------

        punti_assegnati = aggiungi_punti(
            16,
            posizioni_sbagliate
        )


        st.divider()


        # =================================================
        # RISULTATO
        # =================================================

        if posizioni_sbagliate == 0:

            st.success(
                "Mi dispiace le ho azzeccahe tutte!"
            )

            st.write(
                "A quanto pare ti conosco proprio bene. ❤️"
            )

            st.write(
                "🏆 **Hai conquistato 0 punti!**"
            )


        elif posizioni_sbagliate == 5:

            st.warning(
                "😂 Buono, non ne ho azzeccata nemmeno una!"
            )

            st.write(
                "A quanto pare ti conosco molto meno "
                "di quanto pensassi! 😏"
            )

            st.write(
                "🏆 **Hai conquistato 5 punti!**"
            )


        else:

            st.info(
                f"😏 Ho indovinato **{posizioni_corrette} "
                f"posizioni su 5**."
            )

            st.write(
                f"❌ In **{posizioni_sbagliate} posizioni** "
                f"ti conoscevo male!"
            )

            st.write(
                f"🏆 **Hai conquistato "
                f"{posizioni_sbagliate} punti!**"
            )


        # =================================================
        # SOLUZIONE
        # =================================================

        st.divider()

        st.subheader(
            "💡 Il mio pronostico"
        )

        for i, attivita in enumerate(
            ordine_corretto,
            start=1
        ):

            st.write(
                f"**{i}. {attivita}**"
            )

        st.caption(
            "Ogni posizione diversa significa che "
            "ti conoscevo un po' meno bene 😂❤️"
        )
