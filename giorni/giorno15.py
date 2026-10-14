
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
        st.write("🏆 Hai già conquistato i 3 punti di questa sfida.")

        st.header("❤️ Giorno 15 — Una cosa per te")

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
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 15 — Una cosa per te")

    st.write(
        "Prima di iniziare la giornata, fermati un attimo."
    )

    st.write(
        "🌱 **Ora devi dirti una cosa carina e stimolante "
        "verso te stesso per iniziare la giornata.**"
    )

    st.write(
        "Non deve essere perfetta. Deve essere qualcosa "
        "che pensi davvero di te."
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

            punti_assegnati = aggiungi_punti(15, 3)

            st.success(
                "🥰 Bravo. Te lo meriti oggi e tutti i giorni. ❤️"
            )

            st.balloons()

            if punti_assegnati:
                st.write(
                    "🏆 **Hai conquistato 3 punti!**"
                )

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
