import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato,
    get_punteggio
)


# =====================================================
# CONFIGURAZIONE
# =====================================================

GIORNO = 24
COMBINAZIONE = "22102024"

# Posizioni delle cifre da rivelare
# (indice 0-based)
POSIZIONI_RIVELATE = {
    1: [2],             # 1 cifra
    2: [0, 4],          # 2 cifre
    3: [0, 2, 7],       # 3 cifre
    4: [0, 2, 5, 7]     # 4 cifre
}

INDIZI = [
    "La somma dei numeri della combinazione è **13**.",
    "Nella combinazione ci sono **tre 2**.",
    "Nella combinazione ci sono **due 0**.",
    "La prima e la seconda cifra sono **uguali**.",
    "La combinazione è composta da **8 cifre**.",
    "Le ultime due cifre sono **24**.",
    "La combinazione contiene una **data importante per noi**. ❤️",
    "È una data che mi ricorda un momento che non dimenticherò. ❤️"
]


# =====================================================
# NUMERO DI CIFRE RIVELATE
# =====================================================

def numero_cifre_rivelate(punteggio):

    if punteggio < 70:
        return 0
    elif punteggio < 80:
        return 1
    elif punteggio < 90:
        return 2
    elif punteggio < 100:
        return 3
    else:
        return 4


# =====================================================
# MOSTRA COMBINAZIONE CON CIFRE RIVELATE
# =====================================================

def mostra_combinazione_rivelata(numero):

    posizioni = POSIZIONI_RIVELATE.get(numero, [])

    caratteri = []

    for i, cifra in enumerate(COMBINAZIONE):

        if i in posizioni:
            caratteri.append(cifra)
        else:
            caratteri.append("•")

    return " ".join(caratteri)


# =====================================================
# GIOCO
# =====================================================

def mostra_gioco():

    # -------------------------------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------------------------------

    if giorno_completato(GIORNO):

        st.success("🔓 Cassaforte già aperta!")
        st.write("🎄 Hai già completato la sfida del Giorno 24.")
        st.write("")
        st.markdown(
            """
            <h2 style="text-align:center;">
            ❤️ Il mio posto preferito è accanto a te.
            </h2>
            """,
            unsafe_allow_html=True
        )

        return

    # -------------------------------------------------
    # INIZIALIZZAZIONE SESSIONE
    # -------------------------------------------------

    if "giorno24_tentativi" not in st.session_state:
        st.session_state.giorno24_tentativi = 0

    # -------------------------------------------------
    # PUNTEGGIO TOTALE
    # -------------------------------------------------

    punteggio = get_punteggio()

    cifre_rivelate = numero_cifre_rivelate(punteggio)

    # -------------------------------------------------
    # TITOLO
    # -------------------------------------------------

    st.header("🔐 Giorno 24 — La cassaforte")

    st.write(
        "Siamo arrivati all'ultima sfida. ❤️"
    )

    st.write(
        "Per aprire la cassaforte devi trovare "
        "**la combinazione segreta di 8 cifre**."
    )

    # -------------------------------------------------
    # PUNTEGGIO
    # -------------------------------------------------

    st.info(
        f"🏆 Il tuo punteggio totale è **{punteggio} punti**."
    )

    # -------------------------------------------------
    # CIFRE RIVELATE
    # -------------------------------------------------

    if cifre_rivelate == 0:

        st.write(
            "😈 Hai meno di 70 punti..."
        )

        st.write(
            "Questa volta non ti regalo nemmeno una cifra. 😂"
        )

        st.markdown(
            """
            <h1 style="text-align:center; letter-spacing:12px;">
            • • • • • • • •
            </h1>
            """,
            unsafe_allow_html=True
        )

    else:

        st.write(
            f"🎁 Grazie al tuo punteggio hai sbloccato "
            f"**{cifre_rivelate} "
            f"{'cifra' if cifre_rivelate == 1 else 'cifre'}**!"
        )

        combinazione_visibile = mostra_combinazione_rivelata(
            cifre_rivelate
        )

        st.markdown(
            f"""
            <h1 style="text-align:center; letter-spacing:10px;">
            {combinazione_visibile}
            </h1>
            """,
            unsafe_allow_html=True
        )

    # -------------------------------------------------
    # FASCE PUNTEGGIO
    # -------------------------------------------------

    with st.expander("💡 Come funzionano gli aiuti?"):

        st.write("Il tuo punteggio determina quante cifre puoi vedere:")

        st.write("• **Meno di 70 punti** → nessuna cifra")
        st.write("• **70–79 punti** → 1 cifra")
        st.write("• **80–89 punti** → 2 cifre")
        st.write("• **90–99 punti** → 3 cifre")
        st.write("• **100+ punti** → 4 cifre")

    st.divider()

    # -------------------------------------------------
    # INDIZI SBLOCCATI
    # -------------------------------------------------

    tentativi = st.session_state.giorno24_tentativi

    if tentativi > 0:

        st.subheader("💡 Indizi sbloccati")

        for i in range(min(tentativi, len(INDIZI))):
            st.write(
                f"**Indizio {i + 1}:** {INDIZI[i]}"
            )

    # -------------------------------------------------
    # INSERIMENTO CODICE
    # -------------------------------------------------

    st.subheader("🔢 Inserisci la combinazione")

    codice = st.text_input(
        "Inserisci le 8 cifre della cassaforte:",
        max_chars=8,
        placeholder="••••••••",
        key="giorno24_codice"
    )

    # -------------------------------------------------
    # CONTROLLO
    # -------------------------------------------------

    if st.button(
        "🔓 PROVA AD APRIRE LA CASSAFORTE",
        use_container_width=True
    ):

        # Controllo formato
        if len(codice) != 8 or not codice.isdigit():

            st.warning(
                "⚠️ La combinazione deve essere composta "
                "da esattamente 8 cifre."
            )

            return

        # -------------------------------------------------
        # CODICE CORRETTO
        # -------------------------------------------------

        if codice == COMBINAZIONE:

            # Il Giorno 24 assegna 0 punti:
            # serve solo a registrarlo come completato.
            completato = aggiungi_punti(GIORNO, 0)

            if completato:

                st.balloons()

                st.divider()

                st.markdown(
                    """
                    <h1 style="text-align:center;">
                    🔓 CASSAFORTE SBLOCCATA
                    </h1>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <h2 style="text-align:center;">
                    22/10/2024
                    </h2>
                    """,
                    unsafe_allow_html=True
                )

                st.write("")

                st.markdown(
                    """
                    <p style="text-align:center; font-size:20px;">
                    Una data che per noi significa tanto. ❤️
                    </p>
                    """,
                    unsafe_allow_html=True
                )

                st.write("")

                st.markdown(
                    """
                    <p style="text-align:center; font-size:20px;">
                    Domani è Natale. 🎄
                    </p>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <h2 style="text-align:center;">
                    E tra tutti i posti in cui potrei essere,
                    <br>
                    il mio posto preferito è accanto a te. ❤️
                    </h2>
                    """,
                    unsafe_allow_html=True
                )

                st.write("")

                st.markdown(
                    """
                    <h2 style="text-align:center;">
                    Buon Natale, amore mio. 🎄❤️
                    </h2>
                    """,
                    unsafe_allow_html=True
                )

        # -------------------------------------------------
        # CODICE SBAGLIATO
        # -------------------------------------------------

        else:

            st.session_state.giorno24_tentativi += 1

            st.error(
                "❌ La cassaforte non si è aperta..."
            )

            nuovo_indizio = min(
                st.session_state.giorno24_tentativi,
                len(INDIZI)
            )

            if nuovo_indizio <= len(INDIZI):

                st.info(
                    f"💡 Hai sbloccato un nuovo indizio: "
                    f"**Indizio {nuovo_indizio}**"
                )

            st.rerun()
