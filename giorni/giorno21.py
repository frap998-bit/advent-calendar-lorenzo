
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # INIZIALIZZAZIONE
    # =====================================================

    if "giorno21_tentativi" not in st.session_state:
        st.session_state.giorno21_tentativi = 0

    if "giorno21_errore" not in st.session_state:
        st.session_state.giorno21_errore = False

    if "giorno21_finito" not in st.session_state:
        st.session_state.giorno21_finito = False

    if "giorno21_vinto" not in st.session_state:
        st.session_state.giorno21_vinto = False

    # =====================================================
    # TITOLO
    # =====================================================

    st.header("🔐 Giorno 21 — La parola misteriosa")

    # =====================================================
    # RISULTATO DELLA PARTITA APPENA TERMINATA
    # Deve precedere giorno_completato()
    # =====================================================

    if st.session_state.giorno21_finito:

        st.divider()

        if st.session_state.giorno21_vinto:

            st.balloons()
            st.success("🎉 INDOVINATO!")

            st.write("🏆 **Hai conquistato 4 punti!**")

        else:

            st.error("😂 Hai esaurito i 3 tentativi!")

            st.write("🏆 **Hai conquistato 0 punti.**")

        st.write("💡 La parola misteriosa era:")
        st.success("**TOPI**")

        st.divider()
        st.subheader("💡 Rivediamo tutti gli indizi")

        st.write("☀️ **1. Animale**")
        st.write("😂 **2. Plurale**")
        st.write("🎨 **3. Coda**")
        st.write("🍦 **4. Omar e Sofia**")

        return

    # =====================================================
    # CONTROLLO COMPLETAMENTO PRECEDENTE
    # =====================================================

    if giorno_completato(21):

        st.success("✅ Giorno 21 completato!")

        st.header("🔐 La parola misteriosa")

        st.write(
            "Hai già affrontato questa sfida! "
            "Ecco tutti gli indizi e la soluzione. ❤️"
        )

        st.divider()
        st.subheader("💡 Gli indizi")

        st.write("☀️ **1. Animale**")
        st.write("😂 **2. Plurale**")
        st.write("🎨 **3. Coda**")
        st.write("🍦 **4. Omar e Sofia**")

        st.divider()
        st.subheader("🎯 La soluzione")

        st.success("**TOPI**")

        st.write("🏆 Hai già registrato il completamento della sfida.")

        return

    # =====================================================
    # INTRODUZIONE
    # =====================================================

    st.write(
        "C'è una parola che è stata nominata alcune volte "
        "durante la scorsa estate."
    )

    st.write("Hai **3 tentativi** per indovinarla.")

    st.info(
        "🎯 Se indovini la parola conquisti **4 punti**. "
        "Dopo 2 tentativi sbagliati si sbloccherà un nuovo indizio..."
    )

    tentativi = st.session_state.giorno21_tentativi

    # =====================================================
    # INDIZI
    # =====================================================

    st.subheader("💡 Gli indizi")

    st.write("☀️ **1. Animale**")
    st.write("😂 **2. Plurale**")
    st.write("🎨 **3. Coda**")

    if tentativi >= 2:
        st.write("🍦 **4. Omar e Sofia**")
    else:
        st.write("❓ **4. -**")

    # =====================================================
    # DOPO UN ERRORE
    # =====================================================

    if st.session_state.giorno21_errore:

        st.divider()

        if tentativi == 1:
            st.warning("❌ Nooo! Non è questa...")
            st.write("Hai ancora **2 tentativi**.")

        elif tentativi == 2:
            st.warning("❌ Daiii, pensa bene!")
            st.write("Hai ancora **1 tentativo**.")
            st.info("🍦 **Nuovo indizio sbloccato: Omar e Sofia**")

        if st.button(
            "➡️ Prova ancora",
            use_container_width=True
        ):
            st.session_state.giorno21_errore = False
            st.rerun()

        return

    # =====================================================
    # NUMERO TENTATIVO
    # =====================================================

    st.divider()

    st.subheader(f"🎯 Tentativo {tentativi + 1} di 3")

    # =====================================================
    # INSERIMENTO RISPOSTA
    # =====================================================

    risposta = st.text_input(
        "🤔 Qual è la parola misteriosa?",
        max_chars=30,
        key=f"giorno21_tentativo_{tentativi}"
    )

    # =====================================================
    # CONTROLLO RISPOSTA
    # =====================================================

    if st.button(
        "🔎 Prova!",
        use_container_width=True
    ):

        risposta = risposta.strip().lower()

        if not risposta:
            st.warning("Scrivi prima una risposta! 😏")
            return

        # -------------------------------------------------
        # RISPOSTA CORRETTA
        # -------------------------------------------------

        if risposta == "topi":

            salvato = aggiungi_punti(21, 4)

            if not salvato:
                st.warning(
                    "Non è stato possibile registrare il risultato. "
                    "Verifica lo stato del Giorno 21 su Supabase."
                )
                return

            st.session_state.giorno21_finito = True
            st.session_state.giorno21_vinto = True
            st.session_state.giorno21_errore = False

            st.rerun()

        # -------------------------------------------------
        # RISPOSTA SBAGLIATA
        # -------------------------------------------------

        st.session_state.giorno21_tentativi += 1
        tentativi = st.session_state.giorno21_tentativi

        # -------------------------------------------------
        # TERZO ERRORE → FINE GIOCO
        # -------------------------------------------------

        if tentativi >= 3:

            salvato = aggiungi_punti(21, 0)

            if not salvato:
                st.warning(
                    "Non è stato possibile registrare la conclusione "
                    "della sfida. Verifica Supabase."
                )
                return

            st.session_state.giorno21_finito = True
            st.session_state.giorno21_vinto = False
            st.session_state.giorno21_errore = False

            st.rerun()

        # -------------------------------------------------
        # PRIMO / SECONDO ERRORE
        # -------------------------------------------------

        st.session_state.giorno21_errore = True
        st.rerun()
