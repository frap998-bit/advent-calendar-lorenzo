import streamlit as st

from utils.punteggio import (
    aggiungi_punti,
    giorno_completato
)


def mostra_gioco():
    if giorno_completato(8):
        st.success("✅ Giorno 8 completato!")
        st.write("🏆 Hai già conquistato i punti di questa sfida.")
        return

    st.header("🚦 Giorno 8 — Il semaforo delle coppie")

    st.write(
        "Oggi devi cercare di capire **come reagirei io** "
        "in alcune situazioni. ❤️"
    )

    st.info(
        "🎯 Hai un solo tentativo. "
        "Ogni risposta corretta vale 1 punto, "
        "per un massimo di 4 punti!"
    )

    domande = [
        {
            "situazione": (
                "🎁 Tu mi fai un regalo e mi dici che devo aspettare "
                "**2 giorni prima di aprirlo**, e che non posso farti domande."
            ),
            "opzioni": [
                "🟢 Easy, attendo senza problemi",
                "🟡 Provo con fatica a non fare domande",
                "🔴 Impossibile, inizio subito a fare domande"
            ],
            "corretta": "🔴 Impossibile, inizio subito a fare domande"
        },
        {
            "situazione": (
                "📸 Abbiamo fatto una bella foto insieme, ma "
                "**penso di essere venuta male**."
            ),
            "opzioni": [
                "🟢 Mi importa solo che sia venuto bene tu",
                "🟡 Vabbè, pazienza, la tengo comunque",
                "🔴 No, la cancello subito"
            ],
            "corretta": "🟡 Vabbè, pazienza, la tengo comunque"
        },
        {
            "situazione": (
                "🍽️ Al ristorante ordino un piatto che voglio tantissimo, "
                "ma il cameriere mi dice che **è finito**."
            ),
            "opzioni": [
                "🟢 No problem, provo subito un'altra cosa",
                "🟡 Uffa, valuto le alternative",
                "🔴 Male male, mi passa completamente la voglia di mangiare lì"
            ],
            "corretta": "🟡 Uffa, valuto le alternative"
        },
        {
            "situazione": (
                "⏰ Dobbiamo partire **alle 8:00**."
            ),
            "opzioni": [
                "🟢 Super, alle 7:50 sono già pronta",
                "🟡 Insomma, alle 7:55 sto ancora finendo le ultime cose",
                "🔴 Male male, alle 8:00 devo ancora prepararmi"
            ],
            "corretta": (
                "🟡 Insomma, alle 7:55 sto ancora finendo le ultime cose"
            )
        }
    ]

    risposte = []

    for i, domanda in enumerate(domande, start=1):
        st.write("")
        st.subheader(f"{i}. {domanda['situazione']}")

        risposta = st.radio(
            "Cosa pensi che sceglierei io?",
            domanda["opzioni"],
            key=f"giorno08_domanda{i}"
        )

        risposte.append(risposta)

    st.write("")

    if st.button(
        "🚦 Scopri quanto mi conosci",
        use_container_width=True
    ):
        punti = 0

        for i, domanda in enumerate(domande):
            if risposte[i] == domanda["corretta"]:
                punti += 1

        aggiungi_punti(8, punti)

        st.divider()

        if punti == 4:
            st.success(
                "❤️ PERFETTO! Mi conosci proprio bene!"
            )
            st.balloons()

        elif punti == 3:
            st.success(
                "🥰 Quasi perfetto! Mi conosci molto bene!"
            )

        elif punti == 2:
            st.warning(
                "😏 Metà giuste... non male, ma puoi fare di meglio!"
            )

        elif punti == 1:
            st.warning(
                "😂 Una sola! Forse devi conoscermi un pochino meglio..."
            )

        else:
            st.error(
                "😂 Lorenzo, ma chi hai conosciuto in questi anni?!"
            )

        st.write(
            f"🏆 **Hai conquistato {punti} punti!**"
        )

        errori = []

        for i, domanda in enumerate(domande):
            if risposte[i] != domanda["corretta"]:
                errori.append(i)

        if errori:
            st.write("")
            st.subheader("❤️ Ecco cosa avrei scelto io:")

            for i in errori:
                st.write(
                    f"**{i + 1}.** {domande[i]['corretta']}"
                )

        else:
            st.success(
                "🎉 Hai indovinato tutte le mie risposte!"
            )
