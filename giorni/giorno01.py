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

    st.header("🔢 Giorno 1 — Sudoku")

    st.write(
        "Cominciamo con una piccola sfida!"
    )

    st.write(
        "Completa il Sudoku usando i numeri da 1 a 4. "
        "Ogni numero deve comparire una sola volta "
        "in ogni riga, colonna e quadrato 2×2."
    )

    st.write("### 🎄 Buona fortuna!")

    # -------------------------
    # SOLUZIONE
    # -------------------------

    soluzione = [
        [1, 2, 3, 4],
        [3, 4, 1, 2],
        [2, 1, 4, 3],
        [4, 3, 2, 1]
    ]

    # -------------------------
    # SUDOKU
    # -------------------------

    # Riga 1
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=1,
            disabled=True,
            key="r1c1"
        )

    with col2:
        r1c2 = st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=None,
            placeholder="?",
            key="r1c2"
        )

    with col3:
        st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=3,
            disabled=True,
            key="r1c3"
        )

    with col4:
        r1c4 = st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=None,
            placeholder="?",
            key="r1c4"
        )

    # Riga 2
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        r2c1 = st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=None,
            placeholder="?",
            key="r2c1"
        )

    with col2:
        st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=4,
            disabled=True,
            key="r2c2"
        )

    with col3:
        r2c3 = st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=None,
            placeholder="?",
            key="r2c3"
        )

    with col4:
        st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=2,
            disabled=True,
            key="r2c4"
        )

    # Riga 3
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=2,
            disabled=True,
            key="r3c1"
        )

    with col2:
        r3c2 = st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=None,
            placeholder="?",
            key="r3c2"
        )

    with col3:
        st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=4,
            disabled=True,
            key="r3c3"
        )

    with col4:
        r3c4 = st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=None,
            placeholder="?",
            key="r3c4"
        )

    # Riga 4
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        r4c1 = st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=None,
            placeholder="?",
            key="r4c1"
        )

    with col2:
        st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=3,
            disabled=True,
            key="r4c2"
        )

    with col3:
        r4c3 = st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=None,
            placeholder="?",
            key="r4c3"
        )

    with col4:
        st.number_input(
            " ",
            min_value=1,
            max_value=4,
            value=1,
            disabled=True,
            key="r4c4"
        )

    st.write("")

    # -------------------------
    # CONTROLLO
    # -------------------------

    if st.button(
        "✅ Controlla Sudoku",
        use_container_width=True
    ):

        risposta = [
            [1, r1c2, 3, r1c4],
            [r2c1, 4, r2c3, 2],
            [2, r3c2, 4, r3c4],
            [r4c1, 3, r4c3, 1]
        ]

        # Controlla se è completo
        completo = all(
            valore is not None
            for riga in risposta
            for valore in riga
        )

        if not completo:

            st.warning(
                "⚠️ Completa tutte le caselle!"
            )

        elif risposta == soluzione:

            # Assegna i punti solo la prima volta
            punti_assegnati = aggiungi_punti(1, 5)

            st.success(
                "🎉 PERFETTO! Sudoku completato!"
            )

            st.balloons()

            if punti_assegnati:
                st.write(
                    "🏆 **Hai conquistato 5 punti!**"
                )
            else:
                st.info(
                    "I 5 punti di questo gioco "
                    "sono già stati assegnati 😉"
                )

        else:

            st.error(
                "❌ Non è corretto... Riprova!"
            )
