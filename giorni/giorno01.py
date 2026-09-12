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
    # CSS GRIGLIA
    # -------------------------

    st.markdown(
        """
        <style>

        .sudoku-container {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }

        .sudoku-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            width: min(100%, 360px);
            aspect-ratio: 1 / 1;
            border: 3px solid #333;
        }

        .sudoku-cell {
            display: flex;
            align-items: center;
            justify-content: center;
            border-right: 1px solid #777;
            border-bottom: 1px solid #777;
            font-size: 24px;
            font-weight: bold;
            min-width: 0;
        }

        .sudoku-cell:nth-child(4n) {
            border-right: none;
        }

        .sudoku-cell:nth-child(n+13) {
            border-bottom: none;
        }

        /* Linee più spesse dei quadrati 2×2 */

        .sudoku-cell:nth-child(2),
        .sudoku-cell:nth-child(6),
        .sudoku-cell:nth-child(10),
        .sudoku-cell:nth-child(14) {
            border-right: 3px solid #333;
        }

        .sudoku-cell:nth-child(9),
        .sudoku-cell:nth-child(10),
        .sudoku-cell:nth-child(11),
        .sudoku-cell:nth-child(12) {
            border-top: 3px solid #333;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # -------------------------
    # GRIGLIA VISIVA
    # -------------------------

    st.markdown(
        """
        <div class="sudoku-container">
            <div class="sudoku-grid">

                <div class="sudoku-cell">1</div>
                <div class="sudoku-cell">?</div>
                <div class="sudoku-cell">3</div>
                <div class="sudoku-cell">?</div>

                <div class="sudoku-cell">?</div>
                <div class="sudoku-cell">4</div>
                <div class="sudoku-cell">?</div>
                <div class="sudoku-cell">2</div>

                <div class="sudoku-cell">2</div>
                <div class="sudoku-cell">?</div>
                <div class="sudoku-cell">4</div>
                <div class="sudoku-cell">?</div>

                <div class="sudoku-cell">?</div>
                <div class="sudoku-cell">3</div>
                <div class="sudoku-cell">?</div>
                <div class="sudoku-cell">1</div>

            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.write("")


    # -------------------------
    # INSERIMENTO NUMERI
    # -------------------------

    st.write("### ✏️ Completa le caselle mancanti")

    st.caption(
        "Inserisci i numeri mancanti nell'ordine indicato."
    )


    # 1
    st.write("**1. Riga 1 — seconda casella**")

    r1c2 = st.number_input(
        "Numero",
        min_value=1,
        max_value=4,
        value=None,
        placeholder="?",
        key="r1c2",
        label_visibility="collapsed"
    )


    # 2
    st.write("**2. Riga 1 — quarta casella**")

    r1c4 = st.number_input(
        "Numero",
        min_value=1,
        max_value=4,
        value=None,
        placeholder="?",
        key="r1c4",
        label_visibility="collapsed"
    )


    # 3
    st.write("**3. Riga 2 — prima casella**")

    r2c1 = st.number_input(
        "Numero",
        min_value=1,
        max_value=4,
        value=None,
        placeholder="?",
        key="r2c1",
        label_visibility="collapsed"
    )


    # 4
    st.write("**4. Riga 2 — terza casella**")

    r2c3 = st.number_input(
        "Numero",
        min_value=1,
        max_value=4,
        value=None,
        placeholder="?",
        key="r2c3",
        label_visibility="collapsed"
    )


    # 5
    st.write("**5. Riga 3 — seconda casella**")

    r3c2 = st.number_input(
        "Numero",
        min_value=1,
        max_value=4,
        value=None,
        placeholder="?",
        key="r3c2",
        label_visibility="collapsed"
    )


    # 6
    st.write("**6. Riga 3 — quarta casella**")

    r3c4 = st.number_input(
        "Numero",
        min_value=1,
        max_value=4,
        value=None,
        placeholder="?",
        key="r3c4",
        label_visibility="collapsed"
    )


    # 7
    st.write("**7. Riga 4 — prima casella**")

    r4c1 = st.number_input(
        "Numero",
        min_value=1,
        max_value=4,
        value=None,
        placeholder="?",
        key="r4c1",
        label_visibility="collapsed"
    )


    # 8
    st.write("**8. Riga 4 — terza casella**")

    r4c3 = st.number_input(
        "Numero",
        min_value=1,
        max_value=4,
        value=None,
        placeholder="?",
        key="r4c3",
        label_visibility="collapsed"
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


        # -------------------------
        # CONTROLLO COMPLETAMENTO
        # -------------------------

        completo = all(
            valore is not None
            for riga in risposta
            for valore in riga
        )


        if not completo:

            st.warning(
                "⚠️ Completa tutte le caselle!"
            )


        # -------------------------
        # RISPOSTA CORRETTA
        # -------------------------

        elif risposta == soluzione:

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


        # -------------------------
        # RISPOSTA ERRATA
        # -------------------------

        else:

            st.error(
                "❌ Non è corretto... Riprova!"
            )
