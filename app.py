import streamlit as st
from datetime import date
import importlib

from utils.punteggio import (
    inizializza_punteggio,
    get_punteggio,
    giorno_completato,
    reset_punteggio
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

# True = tutti i giorni sono disponibili per i test
# False = calendario normale, con apertura dal 1 al 24 dicembre
modalita_test = True

inizializza_punteggio()


if "giorno_aperto" not in st.session_state:
    st.session_state.giorno_aperto = None


# -------------------------
# CSS
# -------------------------

st.markdown(
    """
    <style>

    /* -------------------------
       BOTTONI CALENDARIO
       ------------------------- */

    [data-testid="stButton"] button {
        min-height: 60px !important;
        font-size: 1rem !important;
        padding: 0.3rem !important;
    }


    /* -------------------------
       MOBILE
       ------------------------- */

    @media (max-width: 640px) {

        [data-testid="stButton"] button {
            min-height: 55px !important;
            font-size: 0.9rem !important;
            padding: 0.2rem !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PAGINA DEL GIOCO
# =========================================================

if st.session_state.giorno_aperto is not None:

    giorno = st.session_state.giorno_aperto

    # -------------------------
    # FRECCIA PER TORNARE INDIETRO
    # -------------------------

    if st.button(
        "← Torna al calendario",
        key="torna_calendario",
        use_container_width=False
    ):

        st.session_state.giorno_aperto = None
        st.rerun()


    st.divider()


    # -------------------------
    # CARICA IL GIOCO
    # -------------------------

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


# =========================================================
# PAGINA DEL CALENDARIO
# =========================================================

else:

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

    # 5 giorni per riga

    for settimana in range(5):

        colonne = st.columns(
            5,
            gap="small"
        )

        for i in range(5):

            giorno = settimana * 5 + i + 1

            if giorno > 24:
                continue


            # -------------------------
            # DATA DI APERTURA
            # -------------------------

            if modalita_test:

                # In modalità test tutti i giorni
                # sono immediatamente disponibili
                data_apertura = date(2026, 1, 1)

            else:

                # Calendario definitivo:
                # Giorno 1 -> 1 dicembre
                # Giorno 2 -> 2 dicembre
                # ...
                # Giorno 24 -> 24 dicembre

                data_apertura = date(
                    2026,
                    12,
                    giorno
                )


            with colonne[i]:

                # -------------------------
                # GIORNO BLOCCATO
                # -------------------------

                if oggi < data_apertura:

                    st.button(
                        f"🔒 {giorno}",
                        key=f"bloccato_{giorno}",
                        disabled=True,
                        use_container_width=True
                    )


                # -------------------------
                # GIORNO COMPLETATO
                # -------------------------

                elif giorno_completato(giorno):

                    if st.button(
                        f"✅ {giorno}",
                        key=f"giorno_{giorno}",
                        use_container_width=True
                    ):

                        st.session_state.giorno_aperto = giorno
                        st.rerun()


                # -------------------------
                # GIORNO DISPONIBILE
                # -------------------------

                else:

                    if st.button(
                        f"🎁 {giorno}",
                        key=f"giorno_{giorno}",
                        use_container_width=True
                    ):

                        st.session_state.giorno_aperto = giorno
                        st.rerun()


    # -------------------------
    # PUNTEGGIO
    # -------------------------

    st.divider()

    st.subheader("🏆 Il tuo punteggio")

    punteggio = get_punteggio()

    st.progress(
        punteggio / 100
    )

    st.write(
        f"**{punteggio} / 100 punti**"
    )


    # -------------------------
    # RESET
    # -------------------------

    st.divider()

    if st.button(
        "🔄 Reset calendario",
        use_container_width=False
    ):

        if reset_punteggio():

            st.success(
                "✅ Calendario resettato!"
            )

            st.session_state.giorno_aperto = None

            st.rerun()
