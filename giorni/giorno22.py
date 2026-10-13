
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # DOMANDE
    # =====================================================

    domande = [
        {
            "foto": "immagini/Marzo 2025.jpg",
            "domanda": "📅 In che mese e anno è stata scattata?",
            "opzioni": [
                "Luglio 2025",
                "Marzo 2025",
                "Marzo 2026",
                "Dicembre 2024"
            ],
            "corretta": "Marzo 2025"
        },
        {
            "foto": "immagini/Aprile 2025.jpg",
            "domanda": "📅 In che mese e anno è stata scattata?",
            "opzioni": [
                "Agosto 2025",
                "Aprile 2025",
                "Dicembre 2024",
                "Maggio 2026"
            ],
            "corretta": "Aprile 2025"
        },
        {
            "foto": "immagini/Agosto 2026.jpg",
            "domanda": "📅 In che mese e anno è stata scattata?",
            "opzioni": [
                "Agosto 2025",
                "Dicembre 2024",
                "Agosto 2026",
                "Settembre 2026"
            ],
            "corretta": "Agosto 2026"
        },
        {
            "foto": "immagini/Novembre 2024.jpg",
            "domanda": "📅 In che mese e anno è stata scattata?",
            "opzioni": [
                "Luglio 2024",
                "Novembre 2024",
                "Dicembre 2025",
                "Agosto 2025"
            ],
            "corretta": "Novembre 2024"
        }
    ]

    # =====================================================
    # INIZIALIZZAZIONE SESSIONE
    # =====================================================

    if "giorno22_risultati" not in st.session_state:
        st.session_state.giorno22_risultati = None

    if "giorno22_punti_ottenuti" not in st.session_state:
        st.session_state.giorno22_punti_ottenuti = 0

    # =====================================================
    # TITOLO
    # =====================================================

    st.header("📸 Giorno 22 — Indovina il mese!")

    # =====================================================
    # RISULTATI DELLA PARTITA APPENA TERMINATA
    # IMPORTANTE: prima di giorno_completato(22)
    # =====================================================

    if st.session_state.giorno22_risultati is not None:

        risultati = st.session_state.giorno22_risultati
        risposte_corrette = risultati["corrette"]
        risposte_date = risultati["risposte"]

        st.success("🎉 Hai completato la sfida!")

        if risposte_corrette == 4:
            st.balloons()
            st.success("🎉 PERFETTO! Hai riconosciuto tutti i mesi!")

        elif risposte_corrette == 3:
            st.success("🥰 Brava memoria! Ne hai riconosciute 3 su 4!")

        elif risposte_corrette == 2:
            st.warning("😏 Due su quattro! Non male...")

        elif risposte_corrette == 1:
            st.warning("😂 Una sola corretta! Puoi fare meglio...")

        else:
            st.error(
                "😂 Nessuna corretta! La memoria oggi non collabora..."
            )

        st.write(
            f"🏆 **Hai conquistato {risposte_corrette} punti!**"
        )

        st.divider()
        st.subheader("📸 Rivediamo le nostre foto")

        for i, domanda in enumerate(domande):

            st.markdown(f"### {i + 1}. {domanda['domanda']}")

            st.image(
                domanda["foto"],
                use_container_width=True
            )

            if risposte_date[i] == domanda["corretta"]:
                st.success(
                    f"✅ La tua risposta: {risposte_date[i]}"
                )
            else:
                st.error(
                    f"❌ La tua risposta: {risposte_date[i]}"
                )
                st.info(
                    f"💡 La risposta corretta era: "
                    f"**{domanda['corretta']}**"
                )

        return

    # =====================================================
    # CONTROLLO COMPLETAMENTO PRECEDENTE
    # =====================================================

    if giorno_completato(22):

        st.success("✅ Giorno 22 completato!")

        st.write(
            "Hai già partecipato alla sfida! "
            "Ecco le foto e le date corrette per rivivere "
            "i nostri ricordi. ❤️"
        )

        st.divider()
        st.subheader("📅 Le risposte corrette")

        for i, domanda in enumerate(domande, start=1):

            st.markdown(f"### {i}. {domanda['corretta']}")

            st.image(
                domanda["foto"],
                use_container_width=True
            )

        st.divider()
        st.write("🏆 Hai già conquistato i punti di questa sfida!")

        return

    # =====================================================
    # ISTRUZIONI
    # =====================================================

    st.write(
        "Riconosci queste foto e prova a ricordare "
        "quando sono state scattate. ❤️"
    )

    st.info(
        "🎯 Hai un solo tentativo. "
        "Ogni risposta corretta vale 1 punto, "
        "per un massimo di 4 punti!"
    )

    # =====================================================
    # FOTO E RISPOSTE
    # =====================================================

    risposte = []

    for i, domanda in enumerate(domande, start=1):

        st.write("")
        st.subheader(f"{i}. {domanda['domanda']}")

        st.image(
            domanda["foto"],
            use_container_width=True
        )

        risposta = st.radio(
            "Scegli una risposta:",
            domanda["opzioni"],
            key=f"giorno22_domanda{i}"
        )

        risposte.append(risposta)

    st.write("")

    # =====================================================
    # CONTROLLO RISPOSTE
    # =====================================================

    if st.button(
        "🔎 Controlla le risposte",
        use_container_width=True
    ):

        risposte_corrette = sum(
            1
            for i, domanda in enumerate(domande)
            if risposte[i] == domanda["corretta"]
        )

        # -------------------------------------------------
        # ASSEGNAZIONE PUNTI
        # -------------------------------------------------

        salvato = aggiungi_punti(22, risposte_corrette)

        if not salvato:
            st.warning(
                "Non è stato possibile registrare il risultato. "
                "Controlla se il Giorno 22 è già completato "
                "su Supabase."
            )
            return

        # -------------------------------------------------
        # SALVATAGGIO RISULTATO IN SESSIONE
        # -------------------------------------------------

        st.session_state.giorno22_punti_ottenuti = risposte_corrette

        st.session_state.giorno22_risultati = {
            "corrette": risposte_corrette,
            "risposte": risposte.copy()
        }

        st.rerun()
