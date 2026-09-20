import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)

# ============================================================
# CONFIGURAZIONE
# ============================================================

GIORNO = 24
COMBINAZIONE = "22102024"

INDIZI = [
    "💡 La somma dei numeri della combinazione è **13**.",
    "💡 La combinazione contiene **tre 2**.",
    "💡 La combinazione contiene **due 0**.",
    "💡 La prima cifra è uguale alla seconda.",
    "💡 La combinazione rappresenta una **data molto importante per noi**. ❤️",
]


# ============================================================
# PUNTEGGIO TOTALE
# ============================================================

def get_punteggio_totale():
    """
    Inserisci qui la lettura del punteggio totale
    dal tuo sistema Supabase.

    Deve restituire un intero.
    """

    # TODO:
    # collega questa parte alla funzione che usi già
    # per visualizzare il punteggio totale nell'app.

    return 0


# ============================================================
# CIFRE RIVELATE IN BASE AL PUNTEGGIO
# ============================================================

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


# ============================================================
# MOSTRA CODICE
# ============================================================

def mostra_codice(combinazione, cifre_rivelate):

    risultato = ""

    for i, cifra in enumerate(combinazione):

        if i < cifre_rivelate:
            risultato += f"<span style='color:#b22222; font-weight:bold;'>{cifra}</span>"

        else:
            risultato += "<span style='color:#888;'>_</span>"

        if i < len(combinazione) - 1:
            risultato += "&nbsp;&nbsp;"

    st.markdown(
        f"""
        <div style="
            text-align: center;
            font-size: 38px;
            letter-spacing: 6px;
            padding: 20px;
            border: 2px solid #888;
            border-radius: 12px;
            margin: 20px 0;
            background-color: #f7f7f7;
        ">
            {risultato}
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# GIOCO
# ============================================================

def mostra_gioco():

    # --------------------------------------------------------
    # CONTROLLO GIORNO COMPLETATO
    # --------------------------------------------------------

    if giorno_completato(GIORNO):

        st.success("🎄 Giorno 24 completato!")
        st.write("🔓 Hai già aperto la cassaforte.")
        return


    # --------------------------------------------------------
    # INIZIALIZZAZIONE
    # --------------------------------------------------------

    if "giorno24_tentativi" not in st.session_state:
        st.session_state.giorno24_tentativi = 0

    if "giorno24_sbloccato" not in st.session_state:
        st.session_state.giorno24_sbloccato = False


    # --------------------------------------------------------
    # PUNTEGGIO
    # --------------------------------------------------------

    punteggio = get_punteggio_totale()

    cifre_rivelate = numero_cifre_rivelate(punteggio)


    # --------------------------------------------------------
    # TITOLO
    # --------------------------------------------------------

    st.header("🔐 Giorno 24 — La cassaforte finale")

    st.write(
        "Sei arrivato all'ultimo giorno. ❤️"
    )

    st.write(
        "Durante questi 23 giorni hai accumulato punti..."
    )

    st.write(
        "Ma forse non erano soltanto punti. 👀"
    )

    st.info(
        f"🏆 Hai totalizzato **{punteggio} punti**."
    )


    # --------------------------------------------------------
    # SPIEGAZIONE DEL VANTAGGIO
    # --------------------------------------------------------

    if cifre_rivelate == 0:

        st.warning(
            "😈 Hai meno di 70 punti..."
            "\n\n"
            "Per ora la cassaforte non ti rivela nessuna cifra."
        )

    else:

        st.success(
            f"🎁 Grazie ai tuoi {punteggio} punti, "
            f"hai sbloccato **{cifre_rivelate} "
            f"{'cifra' if cifre_rivelate == 1 else 'cifre'}**!"
        )


    # --------------------------------------------------------
    # CODICE
    # --------------------------------------------------------

    st.subheader("🔢 Inserisci il codice")

    mostra_codice(
        COMBINAZIONE,
        cifre_rivelate
    )


    # --------------------------------------------------------
    # INPUT
    # --------------------------------------------------------

    codice_inserito = st.text_input(
        "Codice della cassaforte",
        max_chars=8,
        placeholder="Inserisci 8 cifre...",
        key="giorno24_codice"
    )

    codice_inserito = codice_inserito.strip()


    # --------------------------------------------------------
    # PULSANTE
    # --------------------------------------------------------

    if st.button(
        "🔓 PROVA AD APRIRE LA CASSAFORTE",
        use_container_width=True
    ):

        # --------------------------------------------
        # CONTROLLO INPUT
        # --------------------------------------------

        if not codice_inserito:

            st.warning(
                "Inserisci il codice prima di provare ad aprire la cassaforte. 🔐"
            )

            return


        if not codice_inserito.isdigit():

            st.error(
                "❌ Il codice deve contenere solo numeri."
            )

            return


        if len(codice_inserito) != 8:

            st.error(
                "❌ Il codice deve essere composto da 8 cifre."
            )

            return


        # --------------------------------------------
        # CODICE CORRETTO
        # --------------------------------------------

        if codice_inserito == COMBINAZIONE:

            st.session_state.giorno24_sbloccato = True

            aggiungi_punti(
                GIORNO,
                0
            )

            st.balloons()

            st.divider()

            st.success("🔓 CASSAFORTE SBLOCCATA!")

            st.write("")

            st.markdown(
                """
                <div style="
                    text-align: center;
                    padding: 25px;
                ">

                    <div style="
                        font-size: 22px;
                        margin-bottom: 20px;
                    ">
                        ❤️ 22/10/2024 ❤️
                    </div>

                    <div style="
                        font-size: 18px;
                        margin-bottom: 25px;
                    ">
                        Una data che per noi significa tanto.
                    </div>

                    <div style="
                        font-size: 18px;
                        margin-bottom: 25px;
                    ">
                        Domani è Natale. 🎄
                    </div>

                    <div style="
                        font-size: 28px;
                        font-weight: bold;
                        line-height: 1.5;
                    ">
                        Il mio posto preferito
                        <br>
                        è accanto a te. ❤️
                    </div>

                    <div style="
                        font-size: 18px;
                        margin-top: 30px;
                    ">
                        Buon Natale, amore mio. 🎄❤️
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            return


        # --------------------------------------------
        # CODICE ERRATO
        # --------------------------------------------

        st.session_state.giorno24_tentativi += 1

        tentativi = st.session_state.giorno24_tentativi

        st.error(
            "❌ Codice errato!"
        )

        # --------------------------------------------
        # SBLOCCO INDIZIO
        # --------------------------------------------

        indice_indizio = tentativi - 1

        if indice_indizio < len(INDIZI):

            st.info(
                f"🔎 **Nuovo indizio sbloccato!**\n\n"
                f"{INDIZI[indice_indizio]}"
            )

        else:

            st.info(
                "🔎 Hai già sbloccato tutti gli indizi."
            )
