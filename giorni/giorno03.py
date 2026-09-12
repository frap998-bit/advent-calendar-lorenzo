
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # -------------------------
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # -------------------------

    if giorno_completato(3):
        st.success("✅ Giorno 3 completato!")
        st.write("🏆 Hai già conquistato i 5 punti di questa sfida.")
        return


    # -------------------------
    # TITOLO
    # -------------------------

    st.header("❤️ Giorno 3 — Il nostro cruciverba")

    st.write(
        "Vediamo quanto ti ricordi delle nostre piccole avventure... 👀"
    )

    st.write(
        "Riempi il cruciverba usando le definizioni qui sotto!"
    )


    # -------------------------
    # DEFINIZIONI
    # -------------------------

    st.subheader("⬇️ Verticali")

    st.write(
        "**1.** Non sopporto quando mi dici che “parto in ____”."
    )

    st.write(
        "**3.** Posto dove ho patito il freddo, perché tu invece stavi bene."
    )

    st.write(
        "**4.** Il 2 che ci ha fatto conoscere."
    )

    st.write(
        "**5.** Una volta sei rimasto con lei a terra."
    )


    st.subheader("➡️ Orizzontali")

    st.write(
        "**2.** La cosa che mia mamma ci ha ordinato di sistemare quest’estate."
    )

    st.write(
        "**5.** L'allergia mi impedisce di diventarlo."
    )

    st.write(
        "**6.** L'asino che non è un asino."
    )


    # -------------------------
    # GRIGLIA
    # -------------------------
    #
    # Coordinate:
    #
    #       1
    #       ↓
    #   Q
    #   U
    #   A
    #   R
    #   T
    #   A
    #
    # ALTALENA
    #
    # LIVIGNO ↓
    # LUCA    ↓
    #
    # GOMMA ↓
    # GATTARA →
    #
    # OLMO →
    #
    # -------------------------

    # Parole e posizioni
    parole = {
        "1": ("QUARTA", 0, 0, "V"),
        "2": ("ALTALENA", 5, 0, "H"),
        "3": ("LIVIGNO", 5, 1, "V"),
        "4": ("LUCA", 5, 4, "V"),
        "5v": ("GOMMA", 1, 3, "V"),
        "5h": ("GATTARA", 1, 3, "H"),
        "6": ("OLMO", 11, 1, "H")
    }


    # -------------------------
    # COSTRUZIONE GRIGLIA
    # -------------------------

    celle = {}

    for numero, (parola, r, c, direzione) in parole.items():

        for i, lettera in enumerate(parola):

            if direzione == "H":
                posizione = (r, c + i)
            else:
                posizione = (r + i, c)

            celle[posizione] = {
                "numero": None,
                "lettera": lettera
            }


    # Numerazione delle caselle iniziali
    numeri_iniziali = {
        (0, 0): "1",
        (5, 0): "2",
        (5, 1): "3",
        (5, 4): "4",
        (1, 3): "5",
        (11, 1): "6"
    }

    for posizione, numero in numeri_iniziali.items():
        if posizione in celle:
            celle[posizione]["numero"] = numero


    # -------------------------
    # INPUT DELLE LETTERE
    # -------------------------

    st.subheader("🧩 Completa il cruciverba")

    st.write("Inserisci una lettera per ogni casella:")

    # Dimensioni griglia
    righe = range(0, 12)
    colonne = range(0, 10)

    risposte = {}

    for r in righe:

        cols = st.columns(len(colonne))

        for c in colonne:

            posizione = (r, c)

            if posizione in celle:

                numero = celle[posizione]["numero"]

                if numero:
                    label = f"{numero}"
                else:
                    label = "·"

                with cols[c]:

                    risposte[posizione] = st.text_input(
                        label,
                        max_chars=1,
                        key=f"giorno03_{r}_{c}",
                        label_visibility="visible"
                    )

            else:

                with cols[c]:
                    st.write("⬛")


    st.write("")


    # -------------------------
    # CONTROLLO
    # -------------------------

    if st.button(
        "🔎 Controlla cruciverba",
        use_container_width=True
    ):

        corretto = True

        for posizione, dati in celle.items():

            risposta = risposte.get(posizione, "").strip().upper()

            if risposta != dati["lettera"]:
                corretto = False
                break


        if corretto:

            punti_assegnati = aggiungi_punti(3, 5)

            st.success(
                "🎉 PERFETTO! Hai completato il cruciverba! ❤️"
            )

            st.balloons()

            if punti_assegnati:
                st.write(
                    "🏆 **Hai conquistato 5 punti!**"
                )

        else:

            st.error(
                "❌ Non è ancora corretto!"
            )

            st.info(
                "💡 Controlla bene gli incroci... "
                "alcune risposte dovrebbero aiutarti a trovare le altre! 😉"
            )
