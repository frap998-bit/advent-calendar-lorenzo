
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(20):
        st.success("✅ Giorno 20 completato!")
        st.write("🏆 Hai già conquistato i punti di questa sfida.")
        return

    # =====================================================
    # INIZIALIZZAZIONE SESSIONE
    # =====================================================

    if "giorno20_tentativi" not in st.session_state:
        st.session_state.giorno20_tentativi = 0

    if "giorno20_miglior_risultato" not in st.session_state:
        st.session_state.giorno20_miglior_risultato = 0

    if "giorno20_terminato" not in st.session_state:
        st.session_state.giorno20_terminato = False

    if "giorno20_ultimo_risultato" not in st.session_state:
        st.session_state.giorno20_ultimo_risultato = None

    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 20 — Quizzetto!")

    st.write(
        "Vediamo quante ne riesci ad azzeccare... 👀"
    )

    tentativi_massimi = 3

    # =====================================================
    # DOMANDE
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
            "domanda": "Cosa ti ha fatto acquisire il potere di Maranza quest'estate?",
            "lettere": 7,
            "soluzione": "CANOTTA"
        },
        {
            "numero": 4,
            "domanda": "Il nostro motto? (Sono due parole)",
            "lettere": 10,
            "soluzione": "PIANO PIANO"
        }
    ]

    # =====================================================
    # INPUT E TENTATIVI
    # =====================================================

    if not st.session_state.giorno20_terminato:

        tentativi_usati = st.session_state.giorno20_tentativi
        tentativi_rimanenti = tentativi_massimi - tentativi_usati

        st.progress(
            tentativi_usati / tentativi_massimi,
            text=f"Tentativi utilizzati: {tentativi_usati}/{tentativi_massimi}"
        )

        st.caption(
            f"💡 Hai ancora {tentativi_rimanenti} "
            f"{'tentativo' if tentativi_rimanenti == 1 else 'tentativi'}."
        )

        risposte = {}

        for domanda in domande:

            numero = domanda["numero"]

            st.markdown(
                f"### {numero}. {domanda['domanda']}"
            )

            st.caption(
                f"🔤 {domanda['lettere']} lettere"
            )

            caratteri_massimi = (
                11 if numero == 4
                else domanda["lettere"]
            )

            risposte[numero] = st.text_input(
                f"Risposta {numero}",
                max_chars=caratteri_massimi,
                key=f"giorno20_risposta_{numero}",
                placeholder="Scrivi qui la risposta..."
            )

            st.write("")

        # =================================================
        # CONTROLLO RISPOSTE
        # =================================================

        if st.button(
            "🔎 Controlla risposte",
            use_container_width=True
        ):

            risposte_corrette = 0

            for domanda in domande:

                numero = domanda["numero"]

                soluzione = (
                    domanda["soluzione"]
                    .strip()
                    .upper()
                    .replace(" ", "")
                )

                risposta = (
                    risposte[numero]
                    .strip()
                    .upper()
                    .replace(" ", "")
                )

                if risposta == soluzione:
                    risposte_corrette += 1

            # Aggiorna tentativi e miglior risultato
            st.session_state.giorno20_tentativi += 1

            st.session_state.giorno20_ultimo_risultato = (
                risposte_corrette
            )

            st.session_state.giorno20_miglior_risultato = max(
                st.session_state.giorno20_miglior_risultato,
                risposte_corrette
            )

            # La sfida termina se indovina tutto
            # oppure se esaurisce i 3 tentativi
            if (
                risposte_corrette == len(domande)
                or st.session_state.giorno20_tentativi
                >= tentativi_massimi
            ):

                st.session_state.giorno20_terminato = True

                # Massimo 4 punti, in base al miglior tentativo
                punti_finali = min(
                    st.session_state.giorno20_miglior_risultato,
                    len(domande)
                )

                aggiungi_punti(20, punti_finali)

            st.rerun()

    # =====================================================
    # FEEDBACK DOPO OGNI TENTATIVO
    # =====================================================

    if st.session_state.giorno20_ultimo_risultato is not None:

        corrette = st.session_state.giorno20_ultimo_risultato

        if corrette == len(domande):

            st.success(
                "🎉 PERFETTO! Hai indovinato tutte le risposte! ❤️"
            )

            st.balloons()

        elif not st.session_state.giorno20_terminato:

            st.warning(
                f"Hai indovinato {corrette} risposte su "
                f"{len(domande)}. 😉"
            )

            st.info(
                "💡 Ritenta! Puoi ancora migliorare il tuo punteggio."
            )

    # =====================================================
    # RISULTATO FINALE
    # =====================================================

    if st.session_state.giorno20_terminato:

        punti_finali = st.session_state.giorno20_miglior_risultato

        st.divider()

        st.subheader("🏆 Sfida terminata!")

        st.success(
            f"Hai conquistato {punti_finali} "
            f"{'punto' if punti_finali == 1 else 'punti'} su 4! ❤️"
        )

        st.write(
            f"Il tuo miglior risultato è stato "
            f"**{punti_finali} risposte corrette su 4**."
        )

        # =================================================
        # SOLUZIONI CORRETTE
        # =================================================

        st.markdown("### 💌 Ecco tutte le risposte corrette!")

        for domanda in domande:

            st.markdown(
                f"**{domanda['numero']}. {domanda['domanda']}**"
            )

            st.write(f"✅ {domanda['soluzione']}")

        st.write("")

        st.caption(
            "L'importante è averci provato... "
            "anche se certe cose dovresti saperle! 😂❤️"
        )
