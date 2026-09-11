```python
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(2):
        st.success("✅ Giorno 2 completato!")
        st.write("🏆 Hai già conquistato i 5 punti di questa sfida.")
        return

    # -------------------------
    # TITOLO
    # -------------------------

    st.header("📚 Giorno 2 — Quanto mi conosci?")

    st.write(
        "Vediamo se sai cosa sto leggendo in questo periodo... 👀"
    )

    st.write(
        "### 📖 Quale libro sto leggendo in questo momento?"
    )

    # -------------------------
    # RISPOSTE
    # -------------------------

    risposta = st.radio(
        "Scegli una risposta:",
        [
            "Il nome della rosa — Umberto Eco",
            "La gatta persiana — Alessandro Varaldo",
            "Dieci piccoli indiani — Agatha Christie",
            "Il grande Gatsby — F. Scott Fitzgerald"
        ],
        key="giorno02_risposta"
    )

    st.write("")

    # -------------------------
    # CONTROLLO
    # -------------------------

    if st.button(
        "🔎 Conferma risposta",
        use_container_width=True
    ):

        if risposta == "La gatta persiana — Alessandro Varaldo":

            punti_assegnati = aggiungi_punti(2, 5)

            st.success(
                "🎉 Esatto! Mi conosci proprio bene!"
            )

            st.balloons()

            if punti_assegnati:
                st.write(
                    "🏆 **Hai conquistato 5 punti!**"
                )

        else:

            # Il giorno viene registrato come completato
            # ma con 0 punti
            aggiungi_punti(2, 0)

            st.error(
                "❌ Sbagliato! Hai perso i 5 punti di questa sfida."
            )

            st.info(
                "📖 La risposta corretta era: "
                "**La gatta persiana — Alessandro Varaldo**"
            )
```
