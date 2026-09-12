import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(15):
        st.success("✅ Giorno 15 completato!")
        st.write("🏆 Hai già conquistato i 5 punti di questa sfida.")
        return


    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 15 — Una cosa per te")

    st.write(
        "Prima di iniziare la giornata, fermati un attimo."
    )

    st.write(
        "🌱 **Ora devi dirti una cosa carina e stimolante verso te stesso "
        "per iniziare la giornata.**"
    )

    st.write(
        "Non deve essere perfetta. Deve essere qualcosa che pensi "
        "davvero di te."
    )

    st.write("")


    # =====================================================
    # PRIMA CONFERMA
    # =====================================================

    if "giorno15_prima_conferma" not in st.session_state:
        st.session_state.giorno15_prima_conferma = False


    if not st.session_state.giorno15_prima_conferma:

        if st.button(
            "💭 Fatto!",
            use_container_width=True
        ):

            st.session_state.giorno15_prima_conferma = True
            st.rerun()


    # =====================================================
    # SECONDA CONFERMA
    # =====================================================

    else:

        st.warning(
            "Sicuro che ti sei detto qualcosa di bello? 🥺"
        )

        st.write(
            "Non vale dire una cosa tanto per farlo. "
            "Pensaci davvero: te lo meriti."
        )

        st.write("")

        if st.button(
            "❤️ Sì, me lo sono detto",
            use_container_width=True
        ):

            punti_assegnati = aggiungi_punti(15, 5)

            st.success(
                "🥰 Bravo. Te lo meriti oggi e tutti i giorni. ❤️"
            )

            st.balloons()

            if punti_assegnati:
                st.write(
                    "🏆 **Hai conquistato 5 punti!**"
                )
