
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
        ("📍 DOVE", "A casa Pittoni", 4),
        ("🧩 COME", "Attendendo con ansia", 3),
        ("📅 QUANDO", "Una domenica sera", 2),
        (
            "❤️ PERCHÉ",
            "Perché quella di Marco è la mia preferita…",
            1
        )
    ]

    # =====================================================
    # INIZIALIZZAZIONE
    # =====================================================

    if "giorno07_indizio" not in st.session_state:
        st.session_state.giorno07_indizio = 0

    if "giorno07_risposta_corretta" not in st.session_state:
        st.session_state.giorno07_risposta_corretta = False

    if "giorno07_finito" not in st.session_state:
        st.session_state.giorno07_finito = False

    if "giorno07_punti_ottenuti" not in st.session_state:
        st.session_state.giorno07_punti_ottenuti = 0

    if "giorno07_risposta_errata_finale" not in st.session_state:
        st.session_state.giorno07_risposta_errata_finale = False

    # =====================================================
    # RISULTATO DELLA PARTITA APPENA TERMINATA
    # Questo controllo deve precedere giorno_completato()
    # =====================================================

    if st.session_state.giorno07_risposta_corretta:

        st.header("Giorno 7 — DOVE, COME, QUANDO E PERCHÉ?")

        for titolo, testo, punti in indizi:
            st.subheader(titolo)
            st.info(testo)

        st.success("🎉 Esatto! La parola era **PIZZA**! 🍕")

        st.success(
            f"🏆 Hai conquistato "
            f"**{st.session_state.giorno07_punti_ottenuti} punti!**"
        )

        st.balloons()
        return

    if st.session_state.giorno07_risposta_errata_finale:

        st.header("Giorno 7 — DOVE, COME, QUANDO E PERCHÉ?")

        for titolo, testo, punti in indizi:
            st.subheader(titolo)
            st.info(testo)

        st.error("❌ Hai utilizzato tutti gli indizi!")

        st.warning("🍕 La parola misteriosa era **PIZZA**!")

        st.write("🏆 Hai conquistato **0 punti**.")

        return

    # =====================================================
    # CONTROLLO COMPLETAMENTO PRECEDENTE
    # =====================================================

    if giorno_completato(7):

        st.success("✅ Giorno 7 completato!")

        st.write(
            f"🏆 Hai conquistato "
            f"**{st.session_state.giorno07_punti_ottenuti} punti!**"
            if st.session_state.giorno07_finito
            else "🏆 Hai già conquistato i punti di questa sfida."
        )

        st.header("Giorno 7 — DOVE, COME, QUANDO E PERCHÉ?")

        st.write(
            "Ecco tutti gli indizi che ti hanno portato "
            "alla parola misteriosa! ❤️"
        )

        st.divider()

        for titolo, testo, punti in indizi:
            st.subheader(titolo)
            st.info(testo)

        st.success("🎉 La parola misteriosa era **PIZZA**! 🍕")

        st.caption(
            "A volte le cose più belle iniziano con una pizza. ❤️"
        )

        return

    # =====================================================
    # TITOLO
    # =====================================================

    indizio = st.session_state.giorno07_indizio

    st.header("Giorno 7 — DOVE, COME, QUANDO E PERCHÉ?")

    st.write(
        "Ti darò **4 indizi** per aiutarti a indovinare "
        "una parola misteriosa. 👀"
    )

    st.write("Prima la indovini, più punti guadagni! 🏆")

    # =====================================================
    # MOSTRA GLI INDIZI SBLOCCATI
    # =====================================================

    for i in range(indizio + 1):

        titolo, testo, punti = indizi[i]

        st.subheader(titolo)
        st.info(testo)

        st.caption(f"🏆 Se indovini ora: **{punti} punti**")

    # =====================================================
    # RISPOSTA
    # =====================================================

    risposta = st.text_input(
        "Qual è la parola?",
        key="giorno07_risposta"
    )

    if st.button("💘 Indovina!", use_container_width=True):

        risposta_pulita = risposta.strip().lower()

        # -------------------------------------------------
        # RISPOSTA CORRETTA
        # -------------------------------------------------

        if risposta_pulita == "pizza":

            punti = indizi[indizio][2]

            completato = aggiungi_punti(7, punti)

            if completato:
                st.session_state.giorno07_punti_ottenuti = punti
                st.session_state.giorno07_risposta_corretta = True
                st.session_state.giorno07_finito = True
                st.rerun()

            else:
                st.warning(
                    "Il completamento non è stato registrato. "
                    "Controlla la connessione a Supabase "
                    "o verifica se il giorno risulta già completato."
                )

        # -------------------------------------------------
        # RISPOSTA ERRATA
        # -------------------------------------------------

        else:

            if indizio == 3:

                completato = aggiungi_punti(7, 0)

                if completato:
                    st.session_state.giorno07_punti_ottenuti = 0
                    st.session_state.giorno07_finito = True
                    st.session_state.giorno07_risposta_errata_finale = True
                    st.rerun()

                else:
                    st.warning(
                        "Non è stato possibile registrare "
                        "la conclusione della sfida."
                    )

            else:
                st.error(
                    "❌ Non è questa! Puoi riprovare oppure "
                    "vedere il prossimo indizio."
                )

    # =====================================================
    # PROSSIMO INDIZIO
    # =====================================================

    if indizio < 3:

        if st.button(
            "🔎 Mostra prossimo indizio",
            use_container_width=True
        ):

            st.session_state.giorno07_indizio += 1
            st.rerun()

    else:

        st.divider()

        st.write(
            "❤️ Questo è l'ultimo indizio. "
            "Ora devi aver capito!"
        )
