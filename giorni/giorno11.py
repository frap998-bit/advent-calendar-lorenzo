
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(11):

        st.success("✅ Giorno 11 completato!")
        st.write("🏆 Hai già conquistato i 3 punti di questa sfida.")

        st.header("❤️ Giorno 11 — Una cosa per te")

        st.write(
            "🌱 Prima di iniziare la giornata, ricordati "
            "di dedicare un pensiero bello anche a te stesso."
        )

        st.divider()

        st.markdown(
            """
            <div style="
                text-align: center;
                padding: 20px;
                border-radius: 15px;
                background-color: rgba(233, 30, 99, 0.08);
            ">
                <h2 style="color: #e91e63;">
                    🥰 Te lo meriti.
                </h2>
                <p style="font-size: 18px;">
                    Oggi e tutti i giorni. ❤️
                </p>
                <p style="font-size: 16px;">
                    Non devi essere perfetto per essere una persona speciale.
                    Ricordatelo, soprattutto nei giorni più difficili.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        return

    # =====================================================
    # TITOLO E MESSAGGIO
    # =====================================================

    st.header("❤️ Giorno 11 — Una cosa per te")

    st.write(
        "Oggi niente gioco, ti volevo solo ricordare una cosa..."
    )

    st.write(
        "🌱 **Ti amo tanto e sei una persona speciale ❤️ "
        "Quindi oggi ti regalerò 3 punti meritati per essere così come sei.**"
    )

    st.write("")

    # =====================================================
    # ASSEGNAZIONE IMMEDIATA DEI PUNTI
    # =====================================================

    if st.button("💭 Prendi i punti!", use_container_width=True):

        punti_assegnati = aggiungi_punti(11, 3)

        if punti_assegnati:
            st.session_state.giorno11_risultato_mostrato = True
            st.rerun()

    # =====================================================
    # MESSAGGIO FINALE
    # =====================================================

    if st.session_state.get("giorno11_risultato_mostrato", False):

        st.success("🥰 Bravo. Te lo meriti oggi e tutti i giorni. ❤️")

        st.balloons()

        st.write("🏆 **Hai conquistato 3 punti!**")

        st.markdown(
            """
            <div style="
                text-align: center;
                padding: 20px;
                border-radius: 15px;
                background-color: rgba(233, 30, 99, 0.08);
            ">
                <h2 style="color: #e91e63;">
                    ❤️ Una cosa da ricordare
                </h2>
                <p style="font-size: 18px;">
                    Non devi essere perfetto per essere una persona speciale.
                </p>
                <p style="font-size: 18px;">
                    Credici un po' di più. Te lo meriti.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
