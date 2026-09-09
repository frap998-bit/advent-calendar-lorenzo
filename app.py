import streamlit as st
from datetime import date

# -------------------------
# CONFIGURAZIONE
# -------------------------

st.set_page_config(
    page_title="Il Calendario di Lorenzo 🎄",
    page_icon="🎄",
    layout="centered"
)

# Data di oggi
oggi = date.today()

# -------------------------
# TITOLO
# -------------------------

st.title("🎄 Il Calendario di Lorenzo 🎄")
st.subheader("Dicembre 2026")

st.write(
    "Ogni giorno si aprirà una nuova casella. "
    "Riuscirai ad arrivare a 100 punti? ❤️"
)

st.divider()

# -------------------------
# CALENDARIO
# -------------------------

for settimana in range(6):

    colonne = st.columns(4)

    for i in range(4):

        giorno = settimana * 4 + i + 1

        if giorno > 24:
            continue

        # Data di apertura della casella
        data_apertura = date(2026, 12, giorno)

        with colonne[i]:

            if oggi >= data_apertura:

                if st.button(
                    f"🎁\n\nGiorno {giorno}",
                    key=f"giorno_{giorno}",
                    use_container_width=True
                ):
                    st.success(
                        f"🎉 Hai aperto il giorno {giorno}!"
                    )

            else:

                st.button(
                    f"🔒\n\nGiorno {giorno}",
                    key=f"bloccato_{giorno}",
                    disabled=True,
                    use_container_width=True
                )

st.divider()

# -------------------------
# PUNTEGGIO
# -------------------------

st.subheader("🏆 Il tuo punteggio")

st.progress(0)

st.write("**0 / 100 punti**")
