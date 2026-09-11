import streamlit as st
from datetime import date
import importlib

from utils.punteggio import (
    inizializza_punteggio,
    get_punteggio
)


# -------------------------
# CONFIGURAZIONE
# -------------------------

st.set_page_config(
    page_title="Il Calendario di Lorenzo 🎄",
    page_icon="🎄",
    layout="centered"
)


# -------------------------
# DATA DI OGGI
# -------------------------

oggi = date.today()

# Inizializza il sistema del punteggio
inizializza_punteggio()


# -------------------------
# STATO DELLA SESSIONE
# -------------------------

if "giorno_aperto" not in st.session_state:
    st.session_state.giorno_aperto = None


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
        # PER ORA è settembre per permettere i test
        data_apertura = date(2026, 9, giorno)

        with colonne[i]:

            # -------------------------
            # GIORNO DISPONIBILE
            # -------------------------

            if oggi >= data_apertura:

                if st.button(
                    f"🎁\n\nGiorno {giorno}",
                    key=f"giorno_{giorno}",
                    use_container_width=True
                ):

                    st.session_state.giorno_aperto = giorno

            # -------------------------
            # GIORNO BLOCCATO
            # -------------------------

            else:

                st.button(
                    f"🔒\n\nGiorno {giorno}",
                    key=f"bloccato_{giorno}",
                    disabled=True,
                    use_container_width=True
                )


# -------------------------
# GIOCO DEL GIORNO
# -------------------------

if st.session_state.giorno_aperto is not None:

    giorno = st.session_state.giorno_aperto

    st.divider()

    try:

        # Costruisce automaticamente il nome del file:
        #
        # giorno 1  → giorni.giorno01
        # giorno 2  → giorni.giorno02
        # ...
        # giorno 24 → giorni.giorno24

        modulo = importlib.import_module(
            f"giorni.giorno{giorno:02d}"
        )

        # Cerca la funzione "mostra_gioco"
        mostra_gioco = getattr(
            modulo,
            "mostra_gioco"
        )

        # Mostra il gioco
        mostra_gioco()

    except ModuleNotFoundError:

        st.info(
            f"🎁 Il gioco del Giorno {giorno} "
            "è ancora in preparazione..."
        )

    except AttributeError:

        st.error(
            f"⚠️ Il file del Giorno {giorno} "
            "non contiene la funzione 'mostra_gioco()'."
        )


# -------------------------
# PUNTEGGIO
# -------------------------

st.divider()

st.subheader("🏆 Il tuo punteggio")

# Recupera il punteggio reale
punteggio = get_punteggio()

# Barra di avanzamento
st.progress(punteggio / 100)

# Mostra il punteggio
st.write(
    f"**{punteggio} / 100 punti**"
)
