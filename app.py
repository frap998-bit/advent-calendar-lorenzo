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
# INIZIALIZZAZIONE
# -------------------------

oggi = date.today()

inizializza_punteggio()


# -------------------------
# GIORNO APERTO
# -------------------------

# Recupera il giorno dal link
if "giorno" in st.query_params:

    try:
        giorno_parametro = int(
            st.query_params["giorno"]
        )

        if 1 <= giorno_parametro <= 24:
            st.session_state.giorno_aperto = giorno_parametro

    except ValueError:
        pass


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

caselle = ""

for giorno in range(1, 25):

    # -------------------------
    # DATA DI APERTURA
    # -------------------------
    # MODALITÀ TEST:
    # settembre 2026
    #
    # Per il calendario definitivo:
    # date(2026, 12, giorno)
    # -------------------------

    data_apertura = date(
        2026,
        9,
        giorno
    )

    # -------------------------
    # GIORNO BLOCCATO
    # -------------------------

    if oggi < data_apertura:

        caselle += f"""
        <div class="casella bloccata">
            🔒<br>
            <span>{giorno}</span>
        </div>
        """

    # -------------------------
    # GIORNO COMPLETATO
    # -------------------------

    elif giorno_completato(giorno):

        caselle += f"""
        <a
            href="?giorno={giorno}"
            target="_self"
            class="casella completata"
        >
            ✅<br>
            <span>{giorno}</span>
        </a>
        """

    # -------------------------
    # GIORNO DISPONIBILE
    # -------------------------

    else:

        caselle += f"""
        <a
            href="?giorno={giorno}"
            target="_self"
            class="casella disponibile"
        >
            🎁<br>
            <span>{giorno}</span>
        </a>
        """


# -------------------------
# HTML CALENDARIO
# -------------------------

st.markdown(
    f"""
    <style>

    .calendario {{
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 6px;
        width: 100%;
        max-width: 100%;
        margin: 0 auto;
        box-sizing: border-box;
    }}

    .casella {{
        box-sizing: border-box;
        width: 100%;
        aspect-ratio: 1 / 1;
        min-width: 0;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        border-radius: 10px;
        text-decoration: none;

        font-size: 0.85rem;
        line-height: 1.1;

        padding: 3px;
    }}

    .casella span {{
        font-size: 0.9rem;
        font-weight: 600;
    }}

    .disponibile {{
        background-color: #ffffff;
        border: 2px solid #d62828;
        color: #d62828;
    }}

    .disponibile:hover {{
        background-color: #fff0f0;
    }}

    .completata {{
        background-color: #ffffff;
        border: 2px solid #2e8b57;
        color: #2e8b57;
    }}

    .bloccata {{
        background-color: #eeeeee;
        border: 2px solid #cccccc;
        color: #999999;
    }}

    @media (max-width: 640px) {{

        .calendario {{
            grid-template-columns: repeat(5, minmax(0, 1fr));
            gap: 5px;
        }}

        .casella {{
            border-radius: 8px;
            font-size: 0.7rem;
        }}

        .casella span {{
            font-size: 0.75rem;
        }}
    }}

    </style>

    <div class="calendario">
        {caselle}
    </div>
    """,
    unsafe_allow_html=True
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
