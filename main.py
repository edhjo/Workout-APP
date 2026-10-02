import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="Character Gym Tracker",
    page_icon="🏋️‍♂️",
    layout="wide"
)

DATA_FILE = "progressi.json"

def carica_progressi():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def salva_progressi(registro):
    progressi = carica_progressi()
    progressi.append(registro)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(progressi, f, indent=4, ensure_ascii=False)

# DATABASE DEI PERSONAGGI (Versione 7 Completa)
DATABASE = {
    "Videogiochi": {
        "Kratos": {
            "nome": "Kratos",
            "altezza": "7\'8\" / 234 cm",
            "peso": "280 lbs / 127 kg",
            "bodyfat": "9%",
            "caratteristiche_fisiche": "Upper body molto sviluppato, avambracci possenti, trapezi giganteschi, spaventosa densità muscolare, furioso, tenace e fortissimo",
            "macros": "40% Proteine / 35% Carboidrati / 25% Grassi",
            "programma_nome": "Programma God of War",
            "descrizione": "Programma completo di forza bruta e condizionamento spartano con schede da 5-6 esercizi completi per sessione.",
            "schede_frequenza": {
                "3 Giorni (Full Body Power Heavy)": {
                    "Giorno 1: Potenza Spartana (Full Body A)": [
                        {"esercizio": "Stacco da terra pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Panca piana con bilanciere", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Rematore T-Bar pesante", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Military Press con bilanciere", "serie": "4x6", "recupero": "2 min"},
                        {"esercizio": "Farmers Walk con manubri pesanti", "serie": "4x30 metri", "recupero": "90 sec"},
                        {"esercizio": "Scrollate con manubri (Shrugs)", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Trazione & Gambe Monolitiche (Full Body B)": [
                        {"esercizio": "Squat con bilanciere pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x6", "recupero": "2 min"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno con bilanciere", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Hammer Curl per la presa", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Plank pesato su disco", "serie": "4x60 sec", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Impatto & Massa Titanica (Full Body C)": [
                        {"esercizio": "Panca inclinata con manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Leg Press a 45° pesante", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso con presa stretta", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Alzate laterali pesanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Curl bilanciere dritto EZ", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "French Press su piana", "serie": "4x10", "recupero": "60 sec"}
                    ]
                },
                "4 Giorni (Upper/Lower Heavy Split)": {
                    "Giorno 1: Upper Body Power": [
                        {"esercizio": "Panca piana pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Rematore T-Bar con maniglia V", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Military Press in piedi", "serie": "4x6", "recupero": "2 min"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Scrollate con bilanciere pesante", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Hammer Curl manubri", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Lower Body Power": [
                        {"esercizio": "Squat con bilanciere pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Stacco da terra pesante", "serie": "4x5", "recupero": "3 min"},
                        {"esercizio": "Leg Press a 45°", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Leg Curl sdraiato", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Farmers Walk pesanti", "serie": "4x30 metri", "recupero": "90 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Upper Body Hypertrophy": [
                        {"esercizio": "Panca inclinata con manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Trazioni zavorrate", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Croci ai cavi per il petto", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Pulley basso presa larga", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Alzate laterali ai cavi", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Superset Curl Bicipiti + Pushdown Tricipiti", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Lower Body & Core Titanico": [
                        {"esercizio": "Stacco rumeno con bilanciere", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Affondi camminati con manubri", "serie": "3x10 per gamba", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Scrollate con manubri pesanti", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Ab Wheel Rollout", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Trattenuta isometrica disco (Grip test)", "serie": "3xMax sec", "recupero": "60 sec"}
                    ]
                },
                "5 Giorni (Bro Split Titanico Completo)": {
                    "Giorno 1: Petto della Guerra": [
                        {"esercizio": "Panca piana pesante bilanciere", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Panca inclinata manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip con zavorra", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Panca declinata bilanciere", "serie": "3x10", "recupero": "90 sec"},
                        {"esercizio": "Croci su piana con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Piegamenti sulle braccia zavorrati", "serie": "3xMax", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Schiena Spartana": [
                        {"esercizio": "Stacco da terra pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Rematore T-Bar", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Trazioni alla sbarra presa larga", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa stretta", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Lat Machine avanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Pull-over con manubrio", "serie": "3x12", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Gambe Monolitiche": [
                        {"esercizio": "Squat con bilanciere pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Stacco rumeno", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Leg Press a 45°", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension singolo", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Leg Curl da seduto", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise alla macchina", "serie": "5x15", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Spalle & Trapezi del Titano": [
                        {"esercizio": "Military Press pesante", "serie": "4x6", "recupero": "2 min"},
                        {"esercizio": "Alzate laterali con manubri pesanti", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Arnold Press da seduto", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Scrollate con manubri pesanti", "serie": "5x12", "recupero": "60 sec"},
                        {"esercizio": "Face Pull ai cavi per deltoidi posteriori", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Alzate frontali con disco", "serie": "3x12", "recupero": "60 sec"}
                    ],
                    "Giorno 5: Braccia & Presa di Ferro": [
                        {"esercizio": "Farmers Walk con manubri da 40+ kg", "serie": "4x30 metri", "recupero": "90 sec"},
                        {"esercizio": "Curl bilanciere dritto EZ", "serie": "4x8-10", "recupero": "60 sec"},
                        {"esercizio": "French Press su piana bilanciere EZ", "serie": "4x8-10", "recupero": "60 sec"},
                        {"esercizio": "Hammer Curl alternato per la presa", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti alla corda", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Wrist Curl (Curl per avambracci)", "serie": "4x15", "recupero": "45 sec"}
                    ]
                }
            }
        }
    },
    "Marvel": {
        "Eddie Brock (Venom)": {
            "nome": "Eddie Brock (Venom)",
            "altezza": "6\'3\" / 191 cm",
            "peso": "260 lbs / 118 kg",
            "bodyfat": "10%",
            "caratteristiche_fisiche": "Gabbia toracica enormemente sviluppata, braccia imponenti, dorsali a V marcati, determinato, competitivo e impetuoso",
            "macros": "45% Proteine / 35% Carboidrati / 20% Grassi",
            "programma_nome": "Programma Venom Hypertrophy",
            "descrizione": "Programma ad alto volume e carichi pesanti per ipertrofia massiccia con schede strutturate fino a 6 esercizi per sessione.",
            "schede_frequenza": {
                "3 Giorni (Push / Pull / Legs Hypertrophy)": {
                    "Giorno 1: Spinta Massiccia (Push)": [
                        {"esercizio": "Panca piana con bilanciere", "serie": "4x6-8", "recupero": "2-3 min"},
                        {"esercizio": "Panca inclinata con manubri", "serie": "4x8-10", "recupero": "90 sec"},
                        {"esercizio": "Military Press in piedi", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "3x10", "recupero": "90 sec"},
                        {"esercizio": "Alzate laterali con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "French Press con bilanciere EZ", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Trazione & Dorsali V-Taper (Pull)": [
                        {"esercizio": "Stacco da terra con bilanciere", "serie": "4x5", "recupero": "3 min"},
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Rematore con bilanciere presa supina", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso con triangolo", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Scrollate con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Curl bilanciere EZ da seduto", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Gambe Monolitiche (Legs)": [
                        {"esercizio": "Squat con bilanciere", "serie": "4x6-8", "recupero": "2-3 min"},
                        {"esercizio": "Leg Press a 45°", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno con manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension superset Leg Curl", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"},
                        {"esercizio": "Plank pesato con disco", "serie": "3x60 sec", "recupero": "60 sec"}
                    ]
                },
                "4 Giorni (Upper / Lower High Volume)": {
                    "Giorno 1: Upper Body Power & Thickness": [
                        {"esercizio": "Panca piana bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Rematore con bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Military Press", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele", "serie": "3x10", "recupero": "90 sec"},
                        {"esercizio": "Hammer Curl per bicipiti", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Lower Body Power & Legs": [
                        {"esercizio": "Squat con bilanciere", "serie": "4x6-8", "recupero": "2-3 min"},
                        {"esercizio": "Stacco rumeno bilanciere", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Leg Press 45°", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Affondi camminati", "serie": "3x10 per gamba", "recupero": "90 sec"},
                        {"esercizio": "Calf raise alla pressa", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Crunch ai cavi alti", "serie": "4x15", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Upper Body Hypertrophy": [
                        {"esercizio": "Panca inclinata manubri", "serie": "4x8-10", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa larga", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Croci ai cavi alti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Alzate laterali con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Curl panca Scott", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti corda", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Lower Body & Abs Focus": [
                        {"esercizio": "Stacco da terra pesante", "serie": "4x5", "recupero": "3 min"},
                        {"esercizio": "Leg Press 45° a una gamba", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Leg Extension", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Leg Curl sdraiato", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"},
                        {"esercizio": "Plank pesato su disco", "serie": "3x60 sec", "recupero": "60 sec"}
                    ]
                },
                "5 Giorni (Bro Split Hypertrophy Mass)": {
                    "Giorno 1: Petto & Addome": [
                        {"esercizio": "Panca piana con bilanciere", "serie": "4x6-8", "recupero": "2-3 min"},
                        {"esercizio": "Panca inclinata manubri", "serie": "4x8-10", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "3x10", "recupero": "90 sec"},
                        {"esercizio": "Croci su piana con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Piegamenti zavorrati", "serie": "3xMax", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe alla sbarra", "serie": "4x15", "recupero": "45 sec"}
                    ],
                    "Giorno 2: Schiena & Lombari": [
                        {"esercizio": "Stacco da terra", "serie": "4x5", "recupero": "3 min"},
                        {"esercizio": "Trazioni zavorrate presa stretta", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Rematore con bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa V", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Lat Machine dietro nuca", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Iperestensioni lombari con disco", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Gambe Monolitiche": [
                        {"esercizio": "Squat con bilanciere", "serie": "4x6-8", "recupero": "2-3 min"},
                        {"esercizio": "Leg Press 45°", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Leg Curl sdraiato", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise seduto", "serie": "5x15", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Spalle & Trapezi 3D": [
                        {"esercizio": "Military Press in piedi", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Alzate laterali con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Scrollate pesanti con manubri", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Arnold Press da seduto", "serie": "3x10", "recupero": "90 sec"},
                        {"esercizio": "Face Pull ai cavi", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Alzate frontali con manubri", "serie": "3x12", "recupero": "60 sec"}
                    ],
                    "Giorno 5: Braccia & Femorali": [
                        {"esercizio": "Stacco rumeno con bilanciere", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Curl bilanciere EZ in piedi", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "French Press piana EZ", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Hammer Curl alternato", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti con corda", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Curl concentrato con manubrio", "serie": "3x12", "recupero": "45 sec"}
                    ]
                }
            }
        },
        "Steve Rogers (Capitan America)": {
            "nome": "Steve Rogers (Capitan America)",
            "altezza": "6\'2\" / 188 cm",
            "peso": "220 lbs / 100 kg",
            "bodyfat": "7-8%",
            "caratteristiche_fisiche": "V-Taper perfetto, spalle rotonde e scolpite, vita stretta, agilità sovrumana, doti di leadership, incrollabile e valoroso",
            "macros": "40% Proteine / 40% Carboidrati / 20% Grassi",
            "programma_nome": "Programma Super Soldier Athletic",
            "descrizione": "Programma atletico ed esplosivo con schede di allenamento ricche da 5-6 esercizi per giornata.",
            "schede_frequenza": {
                "3 Giorni (Full Body Super Soldier)": {
                    "Giorno 1: Spinta & Esplosività (Full Body A)": [
                        {"esercizio": "Panca piana bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Military Press da in piedi", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Box Jump esplosivi", "serie": "4x6", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Panca inclinata con manubri", "serie": "3x10", "recupero": "90 sec"},
                        {"esercizio": "Farmers Walk con zavorra", "serie": "4x30 metri", "recupero": "90 sec"}
                    ],
                    "Giorno 2: Trazione & Agilità (Full Body B)": [
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Rematore con bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Power Clean (Girata al petto)", "serie": "4x5", "recupero": "2 min"},
                        {"esercizio": "Pulley basso presa V", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Face Pull ai cavi", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Hammer Curl con manubri", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Gambe & Core Tattico (Full Body C)": [
                        {"esercizio": "Squat con bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Stacco rumeno manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Affondi camminati con manubri", "serie": "3x10 per gamba", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension superset Leg Curl", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe alla sbarra", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Plank pesato su disco", "serie": "3x60 sec", "recupero": "60 sec"}
                    ]
                },
                "4 Giorni (Upper / Lower Super Soldier Split)": {
                    "Giorno 1: Upper Power & Agility": [
                        {"esercizio": "Panca piana bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Military Press da in piedi", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Rematore con bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip con zavorra", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Face Pull per spalle sane", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Lower Power & Explosiveness": [
                        {"esercizio": "Squat con bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Box Jump esplosivi su box alto", "serie": "4x6", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Leg Press 45°", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"},
                        {"esercizio": "Farmers Walk zavorrato", "serie": "4x30 metri", "recupero": "90 sec"}
                    ],
                    "Giorno 3: Upper Hypertrophy & V-Taper": [
                        {"esercizio": "Panca inclinata manubri", "serie": "4x8-10", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa V", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Alzate laterali con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Croci ai cavi alti", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Curl bilanciere EZ", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti cavo", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Core & Tactical Conditioning": [
                        {"esercizio": "Power Clean (Girata)", "serie": "4x5", "recupero": "2 min"},
                        {"esercizio": "Slam Ball a terra", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe sbarra", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Ab Wheel Rollout", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Battle Ropes per condizionamento", "serie": "4x30 sec", "recupero": "45 sec"},
                        {"esercizio": "Plank laterale con torsione", "serie": "3x45 sec per lato", "recupero": "45 sec"}
                    ]
                },
                "5 Giorni (Super Soldier Complete Routine)": {
                    "Giorno 1: Spinta & Spalle (Push)": [
                        {"esercizio": "Panca piana con bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Military Press da in piedi", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Panca inclinata manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Alzate laterali pesanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti corde", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Trazione & Dorsali (Pull)": [
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Rematore con bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa stretta", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Lat Machine avanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Face Pull ai cavi", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Curl manubri alternato", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Gambe & Agilità Atletica": [
                        {"esercizio": "Squat con bilanciere", "serie": "4x6-8", "recupero": "2-3 min"},
                        {"esercizio": "Box Jump esplosivi", "serie": "4x6", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Affondi camminati", "serie": "3x10 per gamba", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Condizionamento Tattico & Grip": [
                        {"esercizio": "Power Clean (Girata)", "serie": "4x5", "recupero": "2 min"},
                        {"esercizio": "Farmers Walk zavorrato", "serie": "4x30 metri", "recupero": "90 sec"},
                        {"esercizio": "Slam Ball esplosiva", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Push Press con manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Trattenuta isometrica alla sbarra", "serie": "3xMax sec", "recupero": "60 sec"},
                        {"esercizio": "Scrollate con bilanciere", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 5: Braccia & Core": [
                        {"esercizio": "Dip con zavorra per tricipiti", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Hammer Curl con manubri", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "French Press su piana bilanciere EZ", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Curl panca Scott", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe sbarra", "serie": "4x15", "recupero": "45 sec"},
                        {"esercizio": "Plank pesato", "serie": "4x60 sec", "recupero": "45 sec"}
                    ]
                }
            }
        }
    },
    "DC": {
        "Clark Kent (Superman)": {
            "nome": "Clark Kent (Superman)",
            "altezza": "6\'3\" / 191 cm",
            "peso": "235 lbs / 107 kg",
            "bodyfat": "6-7%",
            "caratteristiche_fisiche": "Struttura scheletrica imponente, pettorali scultorei, spalle a palla di cannone, calmo, altruista, nobile e invincibile",
            "macros": "35% Proteine / 45% Carboidrati / 20% Grassi",
            "programma_nome": "Programma Man of Steel",
            "descrizione": "Powerbuilding e carico pesante per massa d\'acciaio con schede da 5-6 esercizi per giornata.",
            "schede_frequenza": {
                "3 Giorni (Full Body Power Heavy)": {
                    "Giorno 1: Spinta d'Acciaio (Full Body A)": [
                        {"esercizio": "Panca piana pesante bilanciere", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Squat pesante con bilanciere", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Military Press da seduto", "serie": "4x6", "recupero": "2 min"},
                        {"esercizio": "Panca inclinata manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "French Press con bilanciere EZ", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Calf raise alla pressa", "serie": "4x15", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Trazione del Titano (Full Body B)": [
                        {"esercizio": "Stacco da terra pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x6", "recupero": "2 min"},
                        {"esercizio": "Rematore T-Bar pesante", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa V", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Curl bilanciere dritto EZ", "serie": "4x8", "recupero": "60 sec"},
                        {"esercizio": "Plank pesato con disco", "serie": "4x60 sec", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Spalle & Braccia d'Acciaio (Full Body C)": [
                        {"esercizio": "Military Press pesante in piedi", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Leg Press 45° pesante", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Alzate laterali pesanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Hammer Curl alternato", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti alla corda", "serie": "4x12", "recupero": "60 sec"}
                    ]
                },
                "4 Giorni (Steel Split Power)": {
                    "Giorno 1: Petto & Tricep Power": [
                        {"esercizio": "Panca piana pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Panca inclinata manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Croci su piana con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "French Press piana EZ", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti cavi", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Schiena & Bicep Power": [
                        {"esercizio": "Stacco da terra pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Trazioni zavorrate", "serie": "4x6", "recupero": "2 min"},
                        {"esercizio": "Rematore con bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa V", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Curl bilanciere dritto EZ", "serie": "4x8", "recupero": "60 sec"},
                        {"esercizio": "Hammer Curl con manubri", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Gambe Monolitiche d\'Acciaio": [
                        {"esercizio": "Squat pesante con bilanciere", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Leg Press pesante 45°", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Leg Curl sdraiato", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Spalle & Core Metropoli": [
                        {"esercizio": "Military Press pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Alzate laterali pesanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Arnold Press da seduto", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Scrollate con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Face Pull ai cavi", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe sbarra", "serie": "4x15", "recupero": "45 sec"}
                    ]
                },
                "5 Giorni (Complete Steel Split)": {
                    "Giorno 1: Spinta d'Acciaio (Petto)": [
                        {"esercizio": "Panca piana pesante bilanciere", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Panca inclinata con manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip con zavorra", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Croci ai cavi alti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Piegamenti zavorrati", "serie": "3xMax", "recupero": "60 sec"},
                        {"esercizio": "Pull-over con manubrio", "serie": "3x12", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Trazione del Titano (Schiena)": [
                        {"esercizio": "Stacco da terra pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Trazioni zavorrate presa larga", "serie": "4x6", "recupero": "2 min"},
                        {"esercizio": "Rematore T-Bar pesante", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso con triangolo", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Lat Machine avanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Scrollate con bilanciere", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Gambe d\'Acciaio": [
                        {"esercizio": "Squat pesante con bilanciere", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Leg Press a 45°", "serie": "4x10", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Leg Curl da seduto", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Spalle di Metropoli": [
                        {"esercizio": "Military Press pesante", "serie": "5x5", "recupero": "3 min"},
                        {"esercizio": "Alzate laterali con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Arnold Press da seduto", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Face Pull ai cavi", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Alzate frontali con disco", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Scrollate pesanti con manubri", "serie": "4x15", "recupero": "60 sec"}
                    ],
                    "Giorno 5: Braccia & Dettagli": [
                        {"esercizio": "Curl bilanciere dritto EZ", "serie": "4x8", "recupero": "60 sec"},
                        {"esercizio": "French Press piana EZ", "serie": "4x8", "recupero": "60 sec"},
                        {"esercizio": "Hammer Curl alternato", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti corda", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Curl panca Scott", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe sbarra", "serie": "4x15", "recupero": "45 sec"}
                    ]
                }
            }
        },
        "Bruce Wayne (Batman)": {
            "nome": "Bruce Wayne (Batman)",
            "altezza": "6\'2\" / 188 cm",
            "peso": "210 lbs / 95 kg",
            "bodyfat": "8%",
            "caratteristiche_fisiche": "Corpo denso, muscolatura funzionale e tirata, addominali rocciosi, disciplinato, strategico, oscuro e instancabile",
            "macros": "40% Proteine / 35% Carboidrati / 25% Grassi",
            "programma_nome": "Programma Dark Knight Tactical",
            "descrizione": "Condizionamento atletico, arti marziali e forza pura con schede ricche da 5-6 esercizi per giornata.",
            "schede_frequenza": {
                "3 Giorni (Tactical Conditioning Full)": {
                    "Giorno 1: Potenza Spinta & Core (Full A)": [
                        {"esercizio": "Power Clean / Girata al petto", "serie": "4x5", "recupero": "2 min"},
                        {"esercizio": "Panca inclinata con manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Military Press in piedi", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Ab Wheel Rollout", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Battle Ropes condizionamento", "serie": "4x30 sec", "recupero": "45 sec"}
                    ],
                    "Giorno 2: Trazione & Agilità (Full B)": [
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Front Squat con bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Rematore con bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Farmers Walk pesanti", "serie": "4x30 metri", "recupero": "90 sec"},
                        {"esercizio": "Face Pull ai cavi", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe sbarra", "serie": "4x15", "recupero": "45 sec"}
                    ],
                    "Giorno 3: Condizionamento Tattico (Full C)": [
                        {"esercizio": "Stacco rumeno bilanciere", "serie": "4x8", "recupero": "2 min"},
                        {"esercizio": "Box Jump alti su box", "serie": "4x6", "recupero": "90 sec"},
                        {"esercizio": "Slam Ball a terra", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Push Press con manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Hammer Curl alternato", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Plank pesato su disco", "serie": "4x60 sec", "recupero": "45 sec"}
                    ]
                },
                "4 Giorni (Dark Knight Tactical Split)": {
                    "Giorno 1: Potenza Esplosiva Spinta": [
                        {"esercizio": "Power Clean / Girata al petto", "serie": "4x5", "recupero": "2 min"},
                        {"esercizio": "Panca inclinata con manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Military Press in piedi", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip alle parallele zavorrati", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Alzate laterali con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti corda", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Trazione & Core Tattico": [
                        {"esercizio": "Trazioni alla sbarra zavorrate", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Rematore con bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa stretta", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Farmers Walk con zavorra", "serie": "4x30 metri", "recupero": "90 sec"},
                        {"esercizio": "Face Pull ai cavi", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Hammer Curl per avambracci", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Gambe & Agilità Tattica": [
                        {"esercizio": "Front Squat con bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Box Jump alti su box", "serie": "4x6", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Affondi camminati", "serie": "3x10 per gamba", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension superset Leg Curl", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Combat Conditioning & Core": [
                        {"esercizio": "Battle Ropes per condizionamento", "serie": "5x30 sec", "recupero": "45 sec"},
                        {"esercizio": "Slam Ball esplosiva", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe sbarra", "serie": "4x15", "recupero": "45 sec"},
                        {"esercizio": "Ab Wheel Rollout", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Torso Twist con disco", "serie": "4x20", "recupero": "45 sec"},
                        {"esercizio": "Plank pesato su disco", "serie": "4x60 sec", "recupero": "45 sec"}
                    ]
                },
                "5 Giorni (Complete Martial & Athletic Routine)": {
                    "Giorno 1: Spinta Esplosiva": [
                        {"esercizio": "Power Clean", "serie": "4x5", "recupero": "2 min"},
                        {"esercizio": "Panca inclinata manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Military Press in piedi", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Dip con zavorra", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Croci ai cavi alti", "serie": "3x12", "recupero": "60 sec"},
                        {"esercizio": "Pushdown tricipiti corde", "serie": "4x12", "recupero": "60 sec"}
                    ],
                    "Giorno 2: Trazione Pesante": [
                        {"esercizio": "Trazioni zavorrate", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Rematore bilanciere", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Pulley basso presa V", "serie": "4x10", "recupero": "60 sec"},
                        {"esercizio": "Lat Machine avanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Face Pull ai cavi", "serie": "4x15", "recupero": "60 sec"},
                        {"esercizio": "Curl bilanciere EZ", "serie": "4x10", "recupero": "60 sec"}
                    ],
                    "Giorno 3: Treno Inferiore & Agilità": [
                        {"esercizio": "Front Squat con bilanciere", "serie": "4x6-8", "recupero": "2 min"},
                        {"esercizio": "Box Jump alti", "serie": "4x6", "recupero": "90 sec"},
                        {"esercizio": "Stacco rumeno manubri", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Affondi camminati pesanti", "serie": "3x10 per gamba", "recupero": "90 sec"},
                        {"esercizio": "Leg Extension", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Calf raise in piedi", "serie": "5x15", "recupero": "60 sec"}
                    ],
                    "Giorno 4: Spalle Tattiche & Grip": [
                        {"esercizio": "Military Press pesante", "serie": "4x8", "recupero": "90 sec"},
                        {"esercizio": "Farmers Walk pesanti", "serie": "4x30 metri", "recupero": "90 sec"},
                        {"esercizio": "Alzate laterali pesanti", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Scrollate con manubri", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Push Press manubri", "serie": "3x10", "recupero": "90 sec"},
                        {"esercizio": "Trattenuta isometrica alla sbarra", "serie": "3xMax sec", "recupero": "60 sec"}
                    ],
                    "Giorno 5: Combat Conditioning & Core": [
                        {"esercizio": "Battle Ropes per condizionamento", "serie": "5x30 sec", "recupero": "45 sec"},
                        {"esercizio": "Slam Ball a terra", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Sollevamento gambe sbarra", "serie": "4x15", "recupero": "45 sec"},
                        {"esercizio": "Ab Wheel Rollout", "serie": "4x12", "recupero": "60 sec"},
                        {"esercizio": "Torso Twist con disco", "serie": "4x20", "recupero": "45 sec"},
                        {"esercizio": "Plank pesato su disco", "serie": "4x60 sec", "recupero": "45 sec"}
                    ]
                }
            }
        }
    }
}

# INTERFACCIA STREAMLIT PRINCIPALE
st.title("⚡ CHARACTER GYM TRACKER (Versione Mobile)")
st.sidebar.header("🎯 SELEZIONE SCHEDA")

categoria = st.sidebar.selectbox("1. Categoria:", list(DATABASE.keys()))
personaggio_nome = st.sidebar.selectbox("2. Personaggio / Eroe:", list(DATABASE[categoria].keys()))

char_data = DATABASE[categoria][personaggio_nome]

# Mostra dettagli fisici
with st.expander("📊 Dati Fisici & Programma"):
    st.write(f"**Altezza:** {char_data['altezza']}")
    st.write(f"**Peso:** {char_data['peso']}")
    st.write(f"**Bodyfat:** {char_data['bodyfat']}")
    st.write(f"**Caratteristiche:** {char_data['caratteristiche_fisiche']}")
    st.write(f"**Macros:** {char_data['macros']}")
    st.write(f"**Programma:** {char_data['programma_nome']}")

st.markdown(f"### 💪 Programma di {personaggio_nome}")

frequenze = list(char_data["schede_frequenza"].keys())
freq_scelta = st.selectbox("📅 Seleziona Frequenza Giorni:", frequenze)

scheda_giorni = char_data["schede_frequenza"][freq_scelta]

inputs_sessione = []

for giorno_titolo, esercizi in scheda_giorni.items():
    st.markdown(f"#### 🏋️‍♂️ {giorno_titolo}")
    for ex in esercizi:
        col1, col2, col3 = st.columns([3, 1, 2])
        with col1:
            st.markdown(f"**{ex['esercizio']}**
*(Serie: {ex['serie']} - Rec: {ex['recupero']})*")
        with col2:
            peso_usato = st.text_input("Peso (kg)", key=f"{giorno_titolo}_{ex['esercizio']}_peso")
        with col3:
            note_usate = st.text_input("Note", key=f"{giorno_titolo}_{ex['esercizio']}_note")
        
        inputs_sessione.append({
            "giorno": giorno_titolo,
            "esercizio": ex['esercizio'],
            "peso": peso_usato,
            "note": note_usate
        })
    st.markdown("---")

if st.button("💾 Salva Sessione di Oggi", use_container_width=True):
    data_ora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = {
        "data": data_ora,
        "personaggio": personaggio_nome,
        "frequenza": freq_scelta,
        "esercizi": []
    }
    for item in inputs_sessione:
        if item["peso"] or item["note"]:
            record["esercizi"].append({
                "giorno": item["giorno"],
                "esercizio": item["esercizio"],
                "peso_kg": item["peso"],
                "note": item["note"]
            })
    
    if not record["esercizi"]:
        st.warning("Inserisci almeno un peso o una nota per salvare la sessione.")
    else:
        salva_progressi(record)
        st.success(f"Allenamento di {personaggio_nome} salvato con successo!")

# Sezione Storico
st.markdown("---")
st.subheader("📜 Storico Allenamenti Salvati")
progressi = carica_progressi()
if progressi:
    for idx, reg in enumerate(reversed(progressi)):
        with st.expander(f"Data: {reg['data']} - {reg['personaggio']} ({reg.get('frequenza', '')})"):
            for ex_reg in reg["esercizi"]:
                st.write(f"- **{ex_reg['giorno']}** | *{ex_reg['esercizio']}*: **{ex_reg['peso_kg']} kg** (Note: {ex_reg['note']})")
else:
    st.info("Nessun allenamento salvato finora.")
