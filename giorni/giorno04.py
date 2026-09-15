```python
import streamlit as st

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
    # INIZIALIZZAZIONE
    # =====================================================

    ordine_corretto = [
        "🏐 Beach volley",
        "📺 Guardare serie TV",
        "🎾 Tennis",
        "🧩 Puzzle",
        "🎹 Suonare",
        "📖 Leggere"
    ]


    # Inizializza l'ordine scelto dall'utente
    if "giorno04_ordine" not in st.session_state:

        st.session_state.giorno04_ordine = [
            "🏐 Beach volley",
            "📺 Guardare serie TV",
            "🎾 Tennis",
            "🧩 Puzzle",
            "🎹 Suonare",
            "📖 Leggere"
        ]

        # Mescoliamo l'ordine iniziale
        import random

        random.shuffle(
            st.session_state.giorno04_ordine
        )


    # Numero di tentativi effettuati
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
        "Metti in ordine queste attività dalla **mia preferita "
        "alla meno preferita**."
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
    # VISUALIZZAZIONE ELEMENTI
    # =====================================================

    for i in range(len(ordine)):

        col1, col2, col3 = st.columns(
            [1, 5, 1]
        )


        # -------------------------------------------------
        # NUMERO
        # -------------------------------------------------

        with col1:

            st.write(
                f"**{i + 1}.**"
            )


        # -------------------------------------------------
        # ATTIVITÀ
        # -------------------------------------------------

        with col2:

            st.write(
                ordine[i]
            )


        # -------------------------------------------------
        # PULSANTE SU
        # -------------------------------------------------

        with col3:

            if i > 0:

                if st.button(
                    "⬆️",
                    key=f"giorno04_up_{i}"
                ):

                    ordine[i - 1], ordine[i] = (
                        ordine[i],
                        ordine[i - 1]
                    )

                    st.session_state.giorno04_ordine = ordine

                    st.rerun()


    # =====================================================
    # PULSANTI GIÙ
    # =====================================================

    st.write("")


    for i in range(len(ordine)):

        if i < len(ordine) - 1:

            if st.button(
                f"⬇️ Sposta '{ordine[i]}' giù",
                key=f"giorno04_down_{i}",
                use_container_width=True
            ):

                ordine[i], ordine[i + 1] = (
                    ordine[i + 1],
                    ordine[i]
                )

                st.session_state.giorno04_ordine = ordine

                st.rerun()


    # =====================================================
    # CONTROLLO
    # =====================================================

    st.write("")

    if st.button(
        "💘 Controlla il mio ordine",
        use_container_width=True
    ):

        # Aumenta tentativi
        st.session_state.giorno04_tentativi += 1

        tentativo_corrente = (
            st.session_state.giorno04_tentativi
        )


        # -------------------------------------------------
        # CALCOLO POSIZIONI CORRETTE
        # -------------------------------------------------

        posizioni_corrette = 0

        for i in range(len(ordine)):

            if ordine[i] == ordine_corretto[i]:

                posizioni_corrette += 1


        st.divider()


        # =================================================
        # TUTTO CORRETTO
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
        # TERZO TENTATIVO
        # =================================================

        if tentativo_corrente >= 3:

            punti_assegnati = aggiungi_punti(
                4,
                posizioni_corrette
            )


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
                "💡 Ecco il vero ordine di Francesca"
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
        # PRIMO / SECONDO TENTATIVO
        # =================================================

        st.warning(
            f"🤔 Hai **{posizioni_corrette} su 6** "
            f"attività nella posizione corretta!"
        )


        st.info(
            f"💡 Non è ancora finita! "
            f"Hai ancora **{3 - tentativo_corrente} "
            f"tentativo/i**. Puoi modificare l'ordine e riprovare!"
        )
```
