import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class CharacterGymApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Character Gym Tracker - Allenati come le Leggende")
        self.root.geometry("1050x820")
        self.root.configure(bg="#121212")

        self.db_dir = "database"
        self.progressi_file = "progressi.json"

        self.personaggi = {}
        self.carica_database()
        self.carica_progressi()

        self.mostra_pagina_benvenuto()

    def carica_database(self):
        if not os.path.exists(self.db_dir):
            os.makedirs(self.db_dir)

        for root_dir, _, files in os.walk(self.db_dir):
            for file in files:
                if file.endswith(".json"):
                    full_path = os.path.join(root_dir, file)
                    try:
                        with open(full_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            cat = data.get("categoria", "Altro")
                            nome = data.get("nome", "Sconosciuto")
                            if cat not in self.personaggi:
                                self.personaggi[cat] = {}
                            self.personaggi[cat][nome] = data
                    except Exception as e:
                        print(f"Errore caricamento {full_path}: {e}")

    def carica_progressi(self):
        if os.path.exists(self.progressi_file):
            try:
                with open(self.progressi_file, "r", encoding="utf-8") as f:
                    self.progressi = json.load(f)
            except:
                self.progressi = []
        else:
            self.progressi = []

    def salva_progressi(self, registro):
        self.progressi.append(registro)
        with open(self.progressi_file, "w", encoding="utf-8") as f:
            json.dump(self.progressi, f, indent=4, ensure_ascii=False)

    def mostra_pagina_benvenuto(self):
        for w in self.root.winfo_children():
            w.destroy()

        welcome_frame = tk.Frame(self.root, bg="#1a1a2e")
        welcome_frame.pack(fill="both", expand=True)

        center_box = tk.Frame(welcome_frame, bg="#1a1a2e")
        center_box.place(relx=0.5, rely=0.5, anchor="center")

        lbl_logo = tk.Label(center_box, text="🏋️‍♂️", font=("Helvetica", 60), bg="#1a1a2e", fg="#e94560")
        lbl_logo.pack(pady=(0, 10))

        lbl_title = tk.Label(center_box, text="CHARACTER GYM TRACKER", font=("Helvetica", 26, "bold"), fg="#ffffff", bg="#1a1a2e")
        lbl_title.pack(pady=5)

        lbl_subtitle = tk.Label(center_box, text="Database di Allenamento Eroi, Attori e Leggende del Cinema", font=("Helvetica", 12, "italic"), fg="#a0a0b0", bg="#1a1a2e")
        lbl_subtitle.pack(pady=(0, 30))

        btn_entra = tk.Button(
            center_box, text="🚀 ENTRA NEL DATABASE", font=("Helvetica", 14, "bold"),
            fg="#ffffff", bg="#e94560", activebackground="#0f3460", activeforeground="#ffffff",
            padx=25, pady=12, bd=0, cursor="hand2", command=self.crea_interfaccia_principale
        )
        btn_entra.pack()

    def crea_interfaccia_principale(self):
        for w in self.root.winfo_children():
            w.destroy()

        header_frame = tk.Frame(self.root, bg="#16213e", height=50)
        header_frame.pack(fill="x")

        lbl_head = tk.Label(header_frame, text="⚡ CHARACTER GYM DATABASE", font=("Helvetica", 16, "bold"), fg="#e94560", bg="#16213e", pady=10)
        lbl_head.pack(side="left", padx=20)

        btn_home = tk.Button(header_frame, text="🏠 Home / Benvenuto", font=("Helvetica", 10, "bold"), fg="#ffffff", bg="#0f3460", bd=0, padx=10, pady=5, command=self.mostra_pagina_benvenuto, cursor="hand2")
        btn_home.pack(side="right", padx=20)

        main_layout = tk.PanedWindow(self.root, orient="horizontal", bd=0, bg="#121212")
        main_layout.pack(fill="both", expand=True, padx=10, pady=10)

        self.left_content_frame = ttk.Frame(main_layout)
        main_layout.add(self.left_content_frame)

        right_panel = tk.Frame(main_layout, bg="#1a1a2e", width=320, padx=15, pady=15)
        main_layout.add(right_panel)

        lbl_panel_title = tk.Label(right_panel, text="🎯 SELEZIONE SCHEDA", font=("Helvetica", 12, "bold"), fg="#e94560", bg="#1a1a2e")
        lbl_panel_title.pack(anchor="w", pady=(0, 15))

        # MENU 1: Categorie
        tk.Label(right_panel, text="1. Scompartimento / Categoria:", font=("Helvetica", 10, "bold"), fg="#ffffff", bg="#1a1a2e").pack(anchor="w", pady=(5, 2))
        categorie_disponibili = list(self.personaggi.keys()) if self.personaggi else ["Marvel", "DC", "Persone Famose", "Film", "Videogiochi"]
        self.combo_cat = ttk.Combobox(right_panel, state="readonly", values=categorie_disponibili)
        self.combo_cat.pack(fill="x", pady=(0, 15))
        self.combo_cat.bind("<<ComboboxSelected>>", self.on_categoria_changed)

        # MENU 2: Personaggio
        tk.Label(right_panel, text="2. Personaggio / Attore:", font=("Helvetica", 10, "bold"), fg="#ffffff", bg="#1a1a2e").pack(anchor="w", pady=(5, 2))
        self.combo_char = ttk.Combobox(right_panel, state="readonly")
        self.combo_char.pack(fill="x", pady=(0, 15))
        self.combo_char.bind("<<ComboboxSelected>>", self.on_personaggio_changed)

        # MENU 3: Versione Film
        self.lbl_versione = tk.Label(right_panel, text="3. Fisico / Versione Film:", font=("Helvetica", 10, "bold"), fg="#ffffff", bg="#1a1a2e")
        self.combo_versione = ttk.Combobox(right_panel, state="readonly")
        self.combo_versione.bind("<<ComboboxSelected>>", self.on_versione_changed)

        self.lbl_versione.pack_forget()
        self.combo_versione.pack_forget()

        # MENU 4: Frequenza (3, 4, 5 Giorni)
        self.lbl_frequenza = tk.Label(right_panel, text="📅 Giorni Allenamento:", font=("Helvetica", 10, "bold"), fg="#ffffff", bg="#1a1a2e")
        self.combo_frequenza = ttk.Combobox(right_panel, state="readonly")
        self.combo_frequenza.bind("<<ComboboxSelected>>", self.on_frequenza_changed)

        self.lbl_frequenza.pack_forget()
        self.combo_frequenza.pack_forget()

        if self.personaggi.keys():
            prima_cat = list(self.personaggi.keys())[0]
            self.combo_cat.set(prima_cat)
            self.on_categoria_changed(None)

        self.show_placeholder()

    def show_placeholder(self):
        for widget in self.left_content_frame.winfo_children():
            widget.destroy()
        lbl = ttk.Label(self.left_content_frame, text="👈 Usa i menu a tendina sulla destra per caricare una scheda.", font=("Helvetica", 12, "italic"))
        lbl.pack(expand=True)

    def on_categoria_changed(self, event):
        cat = self.combo_cat.get()
        self.combo_char.set('')
        self.combo_versione.set('')
        self.combo_frequenza.set('')

        self.lbl_versione.pack_forget()
        self.combo_versione.pack_forget()
        self.lbl_frequenza.pack_forget()
        self.combo_frequenza.pack_forget()

        if cat in self.personaggi:
            nomi_personaggi = list(self.personaggi[cat].keys())
            self.combo_char['values'] = nomi_personaggi
            if nomi_personaggi:
                self.combo_char.set(nomi_personaggi[0])
                self.on_personaggio_changed(None)
        else:
            self.combo_char['values'] = []

    def on_personaggio_changed(self, event):
        cat = self.combo_cat.get()
        char_name = self.combo_char.get()

        if not cat or not char_name or cat not in self.personaggi or char_name not in self.personaggi[cat]:
            return

        char_data = self.personaggi[cat][char_name]

        if "versioni" in char_data:
            self.lbl_versione.pack(anchor="w", pady=(5, 2))
            self.combo_versione.pack(fill="x", pady=(0, 15))

            versioni_nomi = list(char_data["versioni"].keys())
            self.combo_versione['values'] = versioni_nomi
            if versioni_nomi:
                self.combo_versione.set(versioni_nomi[0])
                self.on_versione_changed(None)
        else:
            self.lbl_versione.pack_forget()
            self.combo_versione.pack_forget()
            self.setup_frequenza_menu(char_data)

    def on_versione_changed(self, event):
        cat = self.combo_cat.get()
        char_name = self.combo_char.get()
        versione_nome = self.combo_versione.get()

        if cat in self.personaggi and char_name in self.personaggi[cat]:
            char_data = self.personaggi[cat][char_name]
            if "versioni" in char_data and versione_nome in char_data["versioni"]:
                sub_data = char_data["versioni"][versione_nome]
                self.setup_frequenza_menu(sub_data, title_prefix=f"{char_name} ({versione_nome})")

    def setup_frequenza_menu(self, data, title_prefix=None):
        schede_varianti = data.get("schede_frequenza", {})
        if schede_varianti:
            self.lbl_frequenza.pack(anchor="w", pady=(5, 2))
            self.combo_frequenza.pack(fill="x", pady=(0, 15))

            list_freq = list(schede_varianti.keys())
            self.combo_frequenza['values'] = list_freq
            if list_freq:
                self.combo_frequenza.set(list_freq[0])
                self.render_selected_data(data, list_freq[0], title_prefix)
        else:
            self.lbl_frequenza.pack_forget()
            self.combo_frequenza.pack_forget()
            self.display_character_sheet(data, main_title=title_prefix if title_prefix else data.get("nome", ""))

    def on_frequenza_changed(self, event):
        cat = self.combo_cat.get()
        char_name = self.combo_char.get()
        freq_sel = self.combo_frequenza.get()

        if cat in self.personaggi and char_name in self.personaggi[cat]:
            char_data = self.personaggi[cat][char_name]
            if "versioni" in char_data:
                versione_nome = self.combo_versione.get()
                if versione_nome in char_data["versioni"]:
                    sub_data = char_data["versioni"][versione_nome]
                    self.render_selected_data(sub_data, freq_sel, f"{char_name} ({versione_nome})")
            else:
                self.render_selected_data(char_data, freq_sel)

    def render_selected_data(self, data, freq_key, title_prefix=None):
        scheda_target = data.get("schede_frequenza", {}).get(freq_key, {})
        title_to_use = title_prefix if title_prefix else data.get("nome", "")
        full_title = f"{title_to_use} - {freq_key}"
        self.display_character_sheet(data, override_scheda=scheda_target, main_title=full_title)

    def display_character_sheet(self, data, override_scheda=None, main_title=None):
        for widget in self.left_content_frame.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.left_content_frame)
        scrollbar = ttk.Scrollbar(self.left_content_frame, orient="vertical", command=canvas.yview)
        scroll_content = ttk.Frame(canvas)

        scroll_content.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_content, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        titolo_finale = main_title if main_title else data.get("nome", "")
        lbl_nome = tk.Label(scroll_content, text=titolo_finale, font=("Helvetica", 18, "bold"), fg="#111111")
        lbl_nome.pack(anchor="w", padx=10, pady=(10, 5))

        # BOX DATI PERSONAGGIO
        dati_box = ttk.LabelFrame(scroll_content, text="📊 Dati Fisici & Programma")
        dati_box.pack(fill="x", padx=10, pady=5)

        griglia = ttk.Frame(dati_box)
        griglia.pack(fill="x", padx=10, pady=8)

        campi_dati = [
            ("Nome:", data.get("nome", "N/A")),
            ("Altezza:", data.get("altezza", "N/A")),
            ("Peso:", data.get("peso", "N/A")),
            ("Bodyfat:", data.get("bodyfat", "N/A")),
            ("Caratteristiche Fisiche:", data.get("caratteristiche_fisiche", "N/A")),
            ("Macros:", data.get("macros", "N/A")),
            ("Programma:", data.get("programma_nome", "N/A"))
        ]

        for i, (label_text, val_text) in enumerate(campi_dati):
            lbl_key = ttk.Label(griglia, text=label_text, font=("Helvetica", 10, "bold"), width=22, anchor="w")
            lbl_key.grid(row=i, column=0, sticky="nw", pady=3)

            lbl_val = ttk.Label(griglia, text=val_text, font=("Helvetica", 10), wraplength=450, justify="left")
            lbl_val.grid(row=i, column=1, sticky="nw", pady=3)

        if "descrizione" in data:
            desc_box = ttk.LabelFrame(scroll_content, text="📋 Descrizione & Filosofia")
            desc_box.pack(fill="x", padx=10, pady=5)
            lbl_desc = ttk.Label(desc_box, text=data.get("descrizione", ""), wraplength=620, justify="left")
            lbl_desc.pack(padx=10, pady=5)

        scheda = override_scheda if override_scheda is not None else data.get("scheda_allenamento", {})
        inputs_sessione = []

        for giorno_titolo, esercizi in scheda.items():
            giorno_box = ttk.LabelFrame(scroll_content, text=f"💪 {giorno_titolo}")
            giorno_box.pack(fill="x", padx=10, pady=8)

            for ex in esercizi:
                ex_frame = ttk.Frame(giorno_box)
                ex_frame.pack(fill="x", padx=5, pady=5)

                lbl_ex = ttk.Label(ex_frame, text=f"• {ex['esercizio']}  [{ex['serie']} - rec: {ex['recupero']}]", font=("Helvetica", 10, "bold"))
                lbl_ex.pack(anchor="w")

                entry_frame = ttk.Frame(ex_frame)
                entry_frame.pack(anchor="w", padx=15, pady=2)

                ttk.Label(entry_frame, text="Peso usato (kg):").pack(side="left", padx=(0, 5))
                entry_peso = ttk.Entry(entry_frame, width=8)
                entry_peso.pack(side="left", padx=(0, 15))

                ttk.Label(entry_frame, text="Note:").pack(side="left", padx=(0, 5))
                entry_note = ttk.Entry(entry_frame, width=30)
                entry_note.pack(side="left")

                inputs_sessione.append({
                    "giorno": giorno_titolo,
                    "esercizio": ex['esercizio'],
                    "peso": entry_peso,
                    "note": entry_note
                })

        btn_salva = ttk.Button(scroll_content, text="💾 Salva Sessione di Oggi", command=lambda: self.salva_sessione_utente(titolo_finale, inputs_sessione))
        btn_salva.pack(pady=15)

    def salva_sessione_utente(self, char_name, inputs):
        data_ora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record = {
            "data": data_ora,
            "personaggio": char_name,
            "esercizi": []
        }
        for item in inputs:
            peso_val = item["peso"].get()
            note_val = item["note"].get()
            if peso_val or note_val:
                record["esercizi"].append({
                    "giorno": item["giorno"],
                    "esercizio": item["esercizio"],
                    "peso_kg": peso_val,
                    "note": note_val
                })

        if not record["esercizi"]:
            messagebox.showwarning("Attenzione", "Inserisci almeno un dato di peso o nota per salvare.")
            return

        self.salva_progressi(record)
        messagebox.showinfo("Successo", f"Allenamento '{char_name}' registrato con successo!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterGymApp(root)
    root.mainloop()
