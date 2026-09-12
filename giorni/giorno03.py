
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
        st.write("🏆 Hai già conquistato i 5 punti di questa sfida.")
        return


    # =====================================================
    # TITOLO
    # =====================================================

    st.header("❤️ Giorno 3 — Il nostro cruciverba")

    st.write(
        "Vediamo quanto ti ricordi delle nostre piccole avventure... 👀"
    )

    st.write(
        "Riempi il cruciverba usando le definizioni qui sotto!"
    )


    # =====================================================
    # DEFINIZIONI
    # =====================================================

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


    # =====================================================
    # PAROLE DEL CRUCIVERBA
    # =====================================================

    parole = {

        # Verticali
        "1": ("QUARTA", 0, 0, "V"),
        "3": ("LIVIGNO", 5, 1, "V"),
        "4": ("LUCA", 5, 4, "V"),
        "5v": ("GOMMA", 1, 3, "V"),

        # Orizzontali
        "2": ("ALTALENA", 5, 0, "H"),
        "5h": ("GATTARA", 1, 3, "H"),
        "6": ("OLMO", 11, 1, "H")
    }


    # =====================================================
    # COSTRUZIONE DELLE CASELLE
    # =====================================================

    celle = {}

    for numero, (parola, r, c, direzione) in parole.items():

        for i, lettera in enumerate(parola):

            if direzione == "H":
                posizione = (r, c + i)

            else:
                posizione = (r + i, c)


            # Se la casella esiste già significa
            # che siamo in un incrocio.
            if posizione not in celle:

                celle[posizione] = {
                    "lettera": lettera,
                    "numero": None
                }

            else:

                # Controllo di sicurezza:
                # le lettere degli incroci devono coincidere.
                if celle[posizione]["lettera"] != lettera:
                    st.error(
                        f"Errore nel cruciverba alla casella {posizione}."
                    )
                    return


    # =====================================================
    # NUMERI DELLE DEFINIZIONI
    # =====================================================

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


    # =====================================================
    # STILE
    # =====================================================

    st.markdown(
        """
        <style>

        /* -----------------------------------------------
           CONTENITORE DELLA GRIGLIA
        ------------------------------------------------ */

        .cruciverba-scroll {
            width: 100%;
            overflow-x: auto;
            overflow-y: hidden;
            padding: 10px 4px 18px 4px;
            -webkit-overflow-scrolling: touch;
        }


        /* -----------------------------------------------
           GRIGLIA
        ------------------------------------------------ */

        .cruciverba-grid {

            display: grid;

            grid-template-columns:
                repeat(10, 40px);

            grid-template-rows:
                repeat(12, 40px);

            gap: 2px;

            width: max-content;

            margin: 0 auto;
        }


        /* -----------------------------------------------
           CASELLE
        ------------------------------------------------ */

        .cruciverba-cella {

            width: 40px;
            height: 40px;

            position: relative;

            box-sizing: border-box;

            border-radius: 2px;
        }


        /* Casella nera */

        .cruciverba-nera {

            background-color: #222;

            border: 1px solid #222;
        }


        /* Casella bianca */

        .cruciverba-bianca {

            background-color: white;

            border: 1px solid #555;
        }


        /* -----------------------------------------------
           NUMERO
        ------------------------------------------------ */

        .cruciverba-numero {

            position: absolute;

            top: 2px;
            left: 3px;

            font-size: 9px;

            font-weight: bold;

            color: #333;

            line-height: 1;

            pointer-events: none;

            z-index: 1;
        }


        /* -----------------------------------------------
           MOBILE
        ------------------------------------------------ */

        @media (max-width: 600px) {

            .cruciverba-scroll {

                justify-content: flex-start;

                padding-left: 2px;
                padding-right: 2px;
            }

            .cruciverba-grid {

                margin-left: 0;

                grid-template-columns:
                    repeat(10, 36px);

                grid-template-rows:
                    repeat(12, 36px);

                gap: 2px;
            }

            .cruciverba-cella {

                width: 36px;
                height: 36px;
            }

            .cruciverba-numero {

                font-size: 8px;

                top: 2px;
                left: 2px;
            }
        }

        </style>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # TITOLO GRIGLIA
    # =====================================================

    st.subheader("🧩 Completa il cruciverba")

    st.caption(
        "💡 Sul telefono puoi scorrere la griglia lateralmente "
        "se necessario."
    )


    # =====================================================
    # GRIGLIA
    # =====================================================

    risposte = {}


    # Apro il contenitore scrollabile
    st.markdown(
        '<div class="cruciverba-scroll">',
        unsafe_allow_html=True
    )


    # Apro la griglia
    st.markdown(
        '<div class="cruciverba-grid">',
        unsafe_allow_html=True
    )


    for r in range(12):

        # -------------------------------------------------
        # Una riga
        # -------------------------------------------------

        for c in range(10):

            posizione = (r, c)


            # =================================================
            # CASELLA NERA
            # =================================================

            if posizione not in celle:

                st.markdown(
                    """
                    <div class="cruciverba-cella cruciverba-nera">
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                continue


            # =================================================
            # CASELLA BIANCA
            # =================================================

            numero = celle[posizione]["numero"]


            # Numero della casella
            if numero:

                st.markdown(
                    f"""
                    <div
                        class="cruciverba-numero"
                        style="
                            position: relative;
                            height: 0;
                            top: 3px;
                            left: 3px;
                            z-index: 5;
                            pointer-events: none;
                        "
                    >
                        {numero}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            # -------------------------------------------------
            # INPUT
            #
            # Usiamo una colonna Streamlit per ogni casella.
            # La larghezza viene ridotta tramite CSS.
            # -------------------------------------------------

            risposta = st.text_input(
                label=(
                    f"Casella {numero}"
                    if numero
                    else f"Casella {r}-{c}"
                ),
                max_chars=1,
                key=f"giorno03_{r}_{c}",
                label_visibility="collapsed"
            )

            risposte[posizione] = risposta


    # Chiudo la griglia
    st.markdown(
        "</div></div>",
        unsafe_allow_html=True
    )


    # =====================================================
    # CONTROLLO
    # =====================================================

    st.write("")


    if st.button(
        "🔎 Controlla cruciverba",
        use_container_width=True
    ):

        corretto = True


        # -------------------------------------------------
        # Controllo tutte le caselle
        # -------------------------------------------------

        for posizione, dati in celle.items():

            risposta = (
                risposte
                .get(posizione, "")
                .strip()
                .upper()
            )


            if risposta != dati["lettera"]:

                corretto = False

                break


        # =================================================
        # CORRETTO
        # =================================================

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


        # =================================================
        # ERRATO
        # =================================================

        else:

            st.error(
                "❌ Non è ancora corretto!"
            )

            st.info(
                "💡 Controlla bene gli incroci... "
                "alcune risposte dovrebbero aiutarti "
                "a trovare le altre! 😉"
            )
