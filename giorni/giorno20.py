
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # DOMANDE E SOLUZIONI
    # =====================================================

    domande = [
        {
            "numero": 1,
            "domanda": "Come è detto anche il Prof. Omar?",
            "lettere": 9,
            "soluzione": "SCHETTINI"
        },
        {
            "numero": 2,
            "domanda": "Qual è il nostro posto più gettonato per una cena?",
            "lettere": 3,
            "soluzione": "AMO"
        },
        {
            "numero": 3,
            "domanda": "Cosa ti ha fatto acquisire il potere di Maranza?",
            "lettere": 7,
            "soluzione": "CANOTTA"
        },
        {
            "numero": 4,
            "domanda": "Il nostro motto? (Sono due parole)",
            "lettere": 11,
            "soluzione": "PIANO PIANO"
        },
        {
            "numero": 5,
            "domanda": "L'asino che non è un asino.",
            "lettere": 4,
            "soluzione": "OLMO"
        }
    ]

    # =====================================================
    # INIZIALIZZAZIONE SESSIONE
    # =====================================================

    if "giorno20_tentativi" not in st.session_state:
        st.session_state.giorno20_tentativi = 0

    if "giorno20_risultati" not in st.session_state:
        st.session_state.giorno20_risultati = None

    if "giorno20_punti_ottenuti" not in st.session_state:
        st.session_state.giorno20_punti_ottenuti = 0

    if "giorno20_appena_completato" not in st.session_state:
        st.session_state.giorno20_appena_completato = False

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # Mostra questa schermata solo nelle visite successive
    # =====================================================

    if (
        giorno_completato(20)
        and not st.session_state.giorno20_appena_completato
    ):

        st.success("✅ Giorno 20 completato!")

        st.header("❤️ Giorno 20 — Quanto ti ricordi?")

        st.write(
            "Hai già affrontato questa sfida! "
            "Ecco un ripasso delle nostre piccole avventure. 🥰"
        )

        st.divider()
        st.subheader("💡 Le risposte corrette")

        for domanda in domande:
            st.markdown(
                f"**{domanda['numero']}. {domanda['domanda']}**"
            )
            st.success(f"👉 {domanda['soluzione']}")

        st.divider()
        st.write("🏆 Hai già conquistato i punti di questa sfida!")

        return

    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 20 — Quanto ti ricordi?")

    st.write(
        "Vediamo quanto ti ricordi delle nostre piccole avventure... 👀"
    )

    st.write(
        "Rispondi alle domande e prova a indovinare tutte le parole!"
    )

    tentativi = st.session_state.giorno20_tentativi
    tentativi_rimasti = max(0, 3 - tentativi)

    st.info(
        f"🎯 Hai a disposizione **3 tentativi**. "
        f"Te ne rimangono **{tentativi_rimasti}**."
    )

    # =====================================================
    # MOSTRA RISULTATO FINALE
    # =====================================================

    if st.session_state.giorno20_risultati is not None:

        risultati = st.session_state.giorno20_risultati

        risposte_corrette = sum(
            1
            for risultato in risultati
            if risultato["corretta"]
        )

        st.divider()

        if risposte_corrette == len(domande):

            st.success(
                "🎉 BRAVISSIMO! Hai indovinato tutte le risposte! ❤️"
            )

            st.balloons()

        else:

            st.warning(
                f"😏 Tentativi terminati! Hai indovinato "
                f"**{risposte_corrette} su {len(domande)}**."
            )

        st.write(
            f"🏆 **Hai conquistato "
            f"{st.session_state.giorno20_punti_ottenuti} punti!**"
        )

        st.divider()
        st.subheader("💡 Ecco le risposte")

        for risultato in risultati:

            if risultato["corretta"]:

                st.success(
                    f"✅ **{risultato['numero']}. "
                    f"{risultato['domanda']}**\n\n"
                    f"La tua risposta: **{risultato['risposta']}**"
                )

            else:

                risposta_data = (
                    risultato["risposta"]
                    if risultato["risposta"]
                    else "Nessuna risposta"
                )

                st.error(
                    f"❌ **{risultato['numero']}. "
                    f"{risultato['domanda']}**\n\n"
                    f"La tua risposta: **{risposta_data}**"
                )

                st.info(
                    f"👉 La risposta corretta era: "
                    f"**{risultato['soluzione']}**"
                )

        return

    # =====================================================
    # INPUT RISPOSTE
    # =====================================================

    risposte = {}

    for domanda in domande:

        numero = domanda["numero"]

        st.markdown(
            f"### {numero}. {domanda['domanda']}"
        )

        st.caption(
            f"🔤 {domanda['lettere']} lettere"
        )

        risposte[numero] = st.text_input(
            f"Risposta {numero}",
            max_chars=domanda["lettere"],
            key=f"giorno20_risposta_{numero}",
            placeholder="Scrivi qui la risposta..."
        )

        st.write("")

    # =====================================================
    # CONTROLLO RISPOSTE
    # =====================================================

    if st.button(
        "🔎 Controlla risposte",
        use_container_width=True
    ):

        st.session_state.giorno20_tentativi += 1

        tentativo_corrente = st.session_state.giorno20_tentativi

        risposte_corrette = 0
        risultati = []

        # -------------------------------------------------
        # CALCOLO RISULTATI
        # -------------------------------------------------

        for domanda in domande:

            numero = domanda["numero"]
            soluzione = domanda["soluzione"]

            risposta = risposte[numero].strip().upper()

            corretta = risposta == soluzione

            if corretta:
                risposte_corrette += 1

            risultati.append({
                "numero": numero,
                "domanda": domanda["domanda"],
                "risposta": risposta,
                "soluzione": soluzione,
                "corretta": corretta
            })

        # -------------------------------------------------
        # VITTORIA O TERZO TENTATIVO
        # -------------------------------------------------

        if (
            risposte_corrette == len(domande)
            or tentativo_corrente >= 3
        ):

            punti_assegnati = aggiungi_punti(
                20,
                risposte_corrette
            )

            st.session_state.giorno20_punti_ottenuti = (
                risposte_corrette if punti_assegnati else 0
            )

            st.session_state.giorno20_risultati = risultati

            # Evita di mostrare subito la schermata
            # del giorno già completato dopo il rerun.
            st.session_state.giorno20_appena_completato = True

            st.rerun()

        # -------------------------------------------------
        # PRIMO O SECONDO TENTATIVO
        # -------------------------------------------------

        st.divider()

        st.warning(
            f"😏 Hai indovinato **{risposte_corrette} su "
            f"{len(domande)}**!"
        )

        st.info(
            f"💡 Non è ancora finita! Hai ancora "
            f"**{3 - tentativo_corrente} tentativo/i**. Riprova!"
        )

        st.write("### 🔎 Piccolo aiuto...")

        for risultato in risultati:

            if risultato["corretta"]:

                st.success(
                    f"✅ {risultato['numero']}. "
                    "Questa era corretta!"
                )

            else:

                st.warning(
                    f"❌ {risultato['numero']}. "
                    "Questa non è corretta... 🤔"
                )
