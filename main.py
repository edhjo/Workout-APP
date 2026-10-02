import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="Diario Allenamento",
    page_icon="🏋️‍♂️",
    layout="centered"
)


DATA_FILE = "dati_allenamento.json"


def carica_dati():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salva_dato(data, scheda, esercizio, peso, reps, note):
    dati = carica_dati()
    nuovo_record = {
        "Data": data,
        "Scheda": scheda,
        "Esercizio": esercizio,
        "Peso (kg)": peso,
        "Ripetizioni": reps,
        "Note": note
    }
    dati.append(nuovo_record)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=4)


st.title("🏋️‍♂️ Diario D'Allenamento")

menu = st.sidebar.radio("Menu", ["Registra Allenamento", "Storico & Progressi"])

ESERCIZI = {
    "Giorno A - Petto e Tricipiti": [
        "Panca Piana Bilanciere",
        "Panca Inclinata Manubri",
        "Dip alle Parallele",
        "Pushdown Cavo Alto"
    ],
    "Giorno B - Dorso e Bicipiti": [
        "Stacco da Terra",
        "Trazioni alla Sbarra",
        "Rematore Manubrio",
        "Curl con Bilanciere"
    ],
    "Giorno C - Gambe e Spalle": [
        "Squat con Bilanciere",
        "Leg Press",
        "Military Press",
        "Alzate Laterali Manubri"
    ]
}

if menu == "Registra Allenamento":
    st.header("📝 Registra Esercizio")

    # Selezione Scheda e Esercizio
    scheda_scelta = st.selectbox("Seleziona il Giorno / Scheda", list(ESERCIZI.keys()))
    esercizi_disponibili = ESERCIZI[scheda_scelta]
    esercizio_scelto = st.selectbox("Seleziona Esercizio", esercizi_disponibili)
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso Caricato (kg)", min_value=0.0, step=0.5, value=20.0)
    with col2:
        reps = st.number_input("Ripetizioni Eseguite", min_value=1, step=1, value=10)

    data_allenamento = st.date_input("Data", datetime.now())
    note = st.text_input("Note (opzionale)", placeholder="es. Esecuzione pulita, aumenta peso prossimo allenamento")

    if st.button("💾 Salva Serie", use_container_width=True):
        salva_dato(
            data_allenamento.strftime("%Y-%m-%d"),
            scheda_scelta,
            esercizio_scelto,
            peso,
            reps,
            note
        )
        st.success(f"Salvato: **{esercizio_scelto}** - {peso} kg x {reps} reps!")

elif menu == "Storico & Progressi":
    st.header("📊 I Tuoi Progressi")

    dati = carica_dati()

    if not dati:
        st.info("Non hai ancora registrato nessun allenamento. Vai nella sezione 'Registra Allenamento'!")
    else:
        df = pd.DataFrame(dati)

        # Filtro per esercizio
        esercizi_registrati = df["Esercizio"].unique()
        filtro_esercizio = st.selectbox("Filtra per Esercizio", ["Tutti"] + list(esercizi_registrati))

        if filtro_esercizio != "Tutti":
            df_filtrato = df[df["Esercizio"] == filtro_esercizio]
            
            st.subheader(f"Grafico Progressi: {filtro_esercizio}")
            st.line_chart(df_filtrato, x="Data", y="Peso (kg)")
            
            st.dataframe(df_filtrato.sort_values(by="Data", ascending=False), use_container_width=True)
        else:
            st.dataframe(df.sort_values(by="Data", ascending=False), use_container_width=True)
