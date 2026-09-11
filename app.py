import streamlit as st
from datetime import date
import importlib

from utils.punteggio import (
    inizializza_punteggio,
    get_punteggio,
    giorno_completato
)


# -------------------------
# CONFIGURAZIONE PAGINA
# -------------------------

st.set_page_config(
    page_title="Il Calendario di Lorenzo 🎄",
    page_icon="🎄",
    layout="centered"
)


# -------------------------
# CSS
# -------------------------

st.markdown(
    """
    <style>

    /* Mantiene 5 colonne anche su telefono */
    [data-testid="stHorizontalBlock"] {
        flex-wrap: nowrap !important;
        gap: 0.4rem !important;
    }

    [data-testid="column"] {
        min-width: 0 !important;
        width: 20% !important;
        flex: 1 1 20% !important;
    }

    /* Caselle del calendario */
    [data-testid="stButton"] button {
        width: 100%;
        min-height: 70px;
        padding: 0.5rem 0.2rem;
        font-size: 1.2rem;
        font-weight: 600;
    }

    /* Su telefono */
    @media (max-width: 640px) {

        [data-testid="stHorizontalBlock"] {
            flex-wrap: nowrap !important;
            gap: 0.25rem !important;
        }

        [data-testid="column"] {
            width: 20% !important;
            flex: 1 1 20% !important;
            min-width: 0 !important;
        }

        [data-testid="stButton"] button {
            min-height: 60px;
            padding: 0.3rem 0.1rem;
            font-size: 1rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -------------------------
# INIZIALIZZAZIONE
# -------------------------

oggi = date.today()

inizializza_punteggio()

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

# 5 caselle per riga
for settimana in range(5):

    colonne = st.columns(5)

    for i in range(5):

        giorno = settimana * 5 + i + 1

        if giorno > 24:
            continue

        # -------------------------
        # DATA DI APERTURA
        # -------------------------
        # ATTUALMENTE IN MODALITÀ TEST:
        # settembre 2026
        #
        # Quando sarà pronto il calendario,
        # sostituisci 9 con 12.
        # -------------------------

        data_apertura = date(2026, 9, giorno)

        with colonne[i]:

            # -------------------------
            # GIORNO DISPONIBILE
            # -------------------------

            if oggi >= data_apertura:

                if giorno_completato(giorno):

                    if st.button(
                        f"✅ {giorno}",
                        key=f"giorno_{giorno}",
                        use_container_width=True
                    ):
                        st.session_state.giorno_aperto = giorno

                else:

                    if st.button(
                        f"🎁 {giorno}",
                        key=f"giorno_{giorno}",
                        use_container_width=True
                    ):
                        st.session_state.giorno_aperto = giorno

            # -------------------------
            # GIORNO BLOCCATO
            # -------------------------

            else:

                st.button(
                    f"🔒 {giorno}",
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

        modulo = importlib.import_module(
            f"giorni.giorno{giorno:02d}"
        )

        mostra_gioco = getattr(
            modulo,
            "mostra_gioco"
        )

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

punteggio = get_punteggio()

st.progress(punteggio / 100)

st.write(
    f"**{punteggio} / 100 punti**"
)
