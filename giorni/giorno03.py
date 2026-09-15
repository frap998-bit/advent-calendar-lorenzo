```python
import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():

    # =====================================================
    # CONTROLLO GIORNO GIÀ COMPLETATO
    # =====================================================

    if giorno_completato(3):
        st.success("✅ Giorno 3 completato!")
        st.write("🏆 Hai già conquistato i punti di questa sfida.")
        return


    # =====================================================
    # INIZIALIZZAZIONE TENTATIVI
    # =====================================================

    if "giorno03_tentativi" not in st.session_state:
        st.session_state.giorno03_tentativi = 0


    tentativi = st.session_state.giorno03_tentativi

    tentativi_rimasti = 3 - tentativi


    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 3 — Quanto ti ricordi?")

    st.write(
        "Vediamo quanto ti ricordi delle nostre piccole avventure... 👀"
    )

    st.write(
        "Rispondi alle domande e prova a indovinare tutte le parole!"
    )

    st.info(
        f"🎯 Hai a disposizione **3 tentativi**. "
        f"Te ne rimangono **{tentativi_rimasti}**."
    )


    # =====================================================
    # DOMANDE
    # =====================================================

    domande = [
        {
            "numero": 1,
            "domanda": 'Non sopporto quando mi dici che "parto in ____".',
            "lettere": 6,
            "soluzione": "QUARTA"
        },
        {
            "numero": 2,
            "domanda": "La cosa che mia mamma ci ha ordinato di sistemare quest’estate.",
            "lettere": 8,
            "soluzione": "ALTALENA"
        },
        {
            "numero": 3,
            "domanda": "Posto dove ho patito il freddo, perché tu invece stavi bene.",
            "lettere": 7,
            "soluzione": "LIVIGNO"
        },
        {
            "numero": 4,
            "domanda": "Il 2 che ci ha fatto conoscere.",
            "lettere": 4,
            "soluzione": "LUCA"
        },
        {
            "numero": 5,
            "domanda": "L'allergia mi impedisce di diventarlo.",
            "lettere": 7,
            "soluzione": "GATTARA"
        },
        {
            "numero": 6,
            "domanda": "L'asino che non è un asino.",
            "lettere": 4,
            "soluzione": "OLMO"
        }
    ]


    # =====================================================
    # INPUT RISPOSTE
    # =====================================================

    risposte = {}


    for domanda in domande:

        numero = domanda["numero"]
        testo = domanda["domanda"]
        numero_lettere = domanda["lettere"]


        # -------------------------------------------------
        # DOMANDA
        # -------------------------------------------------

        st.markdown(
            f"### {numero}. {testo}"
        )

        st.caption(
            f"🔤 {numero_lettere} lettere"
        )


        # -------------------------------------------------
        # INPUT
        # -------------------------------------------------

        risposte[numero] = st.text_input(
            f"Risposta {numero}",
            max_chars=numero_lettere,
            key=f"giorno03_risposta_{numero}",
            placeholder="Scrivi qui la risposta..."
        )

        st.write("")


    # =====================================================
    # CONTROLLO
    # =====================================================

    if st.button(
        "🔎 Controlla risposte",
        use_container_width=True
    ):

        # Aumenta il numero di tentativi
        st.session_state.giorno03_tentativi += 1

        tentativo_corrente = st.session_state.giorno03_tentativi


        # -------------------------------------------------
        # CALCOLO RISPOSTE CORRETTE
        # -------------------------------------------------

        risposte_corrette = 0

        risultati = []


        for domanda in domande:

            numero = domanda["numero"]

            soluzione = domanda["soluzione"]

            risposta = (
                risposte[numero]
                .strip()
                .upper()
            )


            corretta = risposta == soluzione


            if corretta:
                risposte_corrette += 1


            risultati.append({
                "numero": numero,
                "domanda": domanda["domanda"],
                "risposta": risposta,
                "soluzione": soluzione,
                "corretta": corretta
            })


        # =================================================
        # TUTTO CORRETTO
        # =================================================

        if risposte_corrette == len(domande):

            punti_assegnati = aggiungi_punti(3, 5)

            st.divider()

            st.success(
                "🎉 PERFETTO! Hai indovinato tutte le risposte! ❤️"
            )

            st.balloons()

            if punti_assegnati:

                st.write(
                    "🏆 **Hai conquistato 5 punti!**"
                )

            return


        # =================================================
        # TERZO TENTATIVO
        # =================================================

        if tentativo_corrente >= 3:

            # 1 punto per ogni risposta corretta
            punti_assegnati = aggiungi_punti(
                3,
                risposte_corrette
            )

            st.divider()

            st.warning(
                f"😏 Tentativi terminati! "
                f"Hai indovinato **{risposte_corrette} su "
                f"{len(domande)}**."
            )


            # -------------------------------------------------
            # PUNTEGGIO
            # -------------------------------------------------

            if punti_assegnati:

                st.write(
                    f"🏆 **Hai conquistato {risposte_corrette} punti!**"
                )


            # -------------------------------------------------
            # RISPOSTE CORRETTE
            # -------------------------------------------------

            st.divider()

            st.subheader(
                "💡 Ecco le risposte corrette"
            )


            for risultato in risultati:

                if risultato["corretta"]:

                    st.success(
                        f"✅ **{risultato['numero']}. "
                        f"{risultato['domanda']}**\n\n"
                        f"La tua risposta: "
                        f"**{risultato['risposta']}**"
                    )

                else:

                    risposta_data = risultato["risposta"]

                    if risposta_data == "":
                        risposta_data = "Nessuna risposta"

                    st.error(
                        f"❌ **{risultato['numero']}. "
                        f"{risultato['domanda']}**\n\n"
                        f"La tua risposta: **{risposta_data}**  \n"
                        f"👉 La risposta corretta era: "
                        f"**{risultato['soluzione']}**"
                    )


            return


        # =================================================
        # PRIMO / SECONDO TENTATIVO
        # =================================================

        st.divider()

        st.warning(
            f"😏 Hai indovinato **{risposte_corrette} su "
            f"{len(domande)}**!"
        )

        st.info(
            f"💡 Non è ancora finita! "
            f"Hai ancora **{3 - tentativo_corrente} "
            f"tentativo/i**. Riprova!"
        )


        # -------------------------------------------------
        # MOSTRA SOLO LE RISPOSTE SBAGLIATE
        # -------------------------------------------------

        st.write("### 🔎 Piccolo aiuto...")

        for risultato in risultati:

            if risultato["corretta"]:

                st.success(
                    f"✅ {risultato['numero']}. "
                    f"Questa era corretta!"
                )

            else:

                st.warning(
                    f"❌ {risultato['numero']}. "
                    f"Questa non è corretta... 🤔"
                )
```
