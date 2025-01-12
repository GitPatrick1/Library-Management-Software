import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class Libro:
    def __init__(self, titolo, autore, in_prestito=False):
        self.titolo = titolo
        self.autore = autore
        self.in_prestito = in_prestito

    def to_dict(self):
        return {
            "titolo": self.titolo,
            "autore": self.autore,
            "in_prestito": self.in_prestito
        }

    @staticmethod
    def from_dict(data):
        return Libro(data["titolo"], data["autore"], data["in_prestito"])

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, In prestito: {'Sì' if self.in_prestito else 'No'}"

class Biblioteca:
    def __init__(self):
        self.collezione = []
        self.file_path = "catalogo.json"
        self.carica_catalogo()

    def aggiungi_libro(self, titolo, autore):
        libro = Libro(titolo, autore)
        self.collezione.append(libro)
        self.salva_catalogo()

    def stampa_catalogo(self):
        return '\n'.join([str(libro) for libro in self.collezione])

    def rimuovi_libro(self, indice):
        if 0 <= indice < len(self.collezione):
            self.collezione.pop(indice)
            self.salva_catalogo()
            return "Libro rimosso con successo."
        else:
            return "Indice non valido."

    def ordina_per_titolo(self):
        self.collezione.sort(key=lambda x: x.titolo)
        self.salva_catalogo()
        return "Catalogo ordinato per titolo."

    def ordina_per_autore(self):
        self.collezione.sort(key=lambda x: x.autore)
        self.salva_catalogo()
        return "Catalogo ordinato per autore."

    def presta_libro(self, indice):
        if 0 <= indice < len(self.collezione):
            libro = self.collezione[indice]
            if libro.in_prestito:
                return "Il libro è già in prestito."
            else:
                libro.in_prestito = True
                self.salva_catalogo()
                return "Libro prestato con successo."
        else:
            return "Indice non valido."

    def restituisci_libro(self, indice):
        if 0 <= indice < len(self.collezione):
            libro = self.collezione[indice]
            if not libro.in_prestito:
                return "Il libro non è attualmente in prestito."
            else:
                libro.in_prestito = False
                self.salva_catalogo()
                return "Libro restituito con successo."
        else:
            return "Indice non valido."

    def cerca_per_titolo(self, titolo):
        risultati = [libro for libro in self.collezione if titolo.lower() in libro.titolo.lower()]
        return risultati

    def salva_catalogo(self):
        with open(self.file_path, "w") as f:
            json.dump([libro.to_dict() for libro in self.collezione], f)

    def carica_catalogo(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.collezione = [Libro.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.collezione = []

class InterfacciaGrafica:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.root = root
        self.root.title("Gestione Biblioteca")
        self.root.geometry("1000x600")
        self.root.config(bg="#F4E1C1")

        self.crea_widgets()

    def crea_widgets(self):
        self.main_frame = tk.Frame(self.root, bg="#F4E1C1")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.catalogo_frame = tk.Frame(self.main_frame, bg="#F4E1C1", width=600)
        self.catalogo_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.titolo_label = tk.Label(self.catalogo_frame, text="Gestione Biblioteca", font=("Helvetica", 24, "bold"), bg="#F4E1C1", fg="#8B4513")
        self.titolo_label.pack(pady=20)

        self.catalogo_label = tk.Label(self.catalogo_frame, text="Catalogo:", font=("Helvetica", 16), bg="#F4E1C1", fg="#8B4513")
        self.catalogo_label.pack()

        self.catalogo_text = tk.Text(self.catalogo_frame, width=70, height=15, wrap="word", font=("Helvetica", 12), bg="#FFF5E1", fg="#8B4513", state=tk.DISABLED)
        self.catalogo_text.pack(pady=10)

        self.form_frame = tk.Frame(self.catalogo_frame, bg="#F4E1C1")
        self.form_frame.pack(pady=10)

        self.titolo_label_form = tk.Label(self.form_frame, text="Titolo:", font=("Helvetica", 12), bg="#F4E1C1", fg="#8B4513")
        self.titolo_label_form.grid(row=0, column=0, padx=10)

        self.titolo_entry = tk.Entry(self.form_frame, font=("Helvetica", 12), bg="#FFF5E1", fg="#8B4513")
        self.titolo_entry.grid(row=0, column=1, padx=10)

        self.autore_label_form = tk.Label(self.form_frame, text="Autore:", font=("Helvetica", 12), bg="#F4E1C1", fg="#8B4513")
        self.autore_label_form.grid(row=1, column=0, padx=10)

        self.autore_entry = tk.Entry(self.form_frame, font=("Helvetica", 12), bg="#FFF5E1", fg="#8B4513")
        self.autore_entry.grid(row=1, column=1, padx=10)

        self.bottoni_frame = tk.Frame(self.main_frame, bg="#F4E1C1", width=400)
        self.bottoni_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        button_width = 15

        self.bottone_aggiungi = tk.Button(self.bottoni_frame, text="Aggiungi Libro", font=("Helvetica", 14), bg="#228B22", fg="white", command=self.aggiungi_libro, width=button_width)
        self.bottone_aggiungi.pack(pady=5)

        self.bottone_stampa = tk.Button(self.bottoni_frame, text="Stampa Catalogo", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.stampa_catalogo, width=button_width)
        self.bottone_stampa.pack(pady=5)

        self.bottone_ordinare_titolo = tk.Button(self.bottoni_frame, text="Ordina per Titolo", font=("Helvetica", 14), bg="#FFD700", fg="white", command=self.ordina_per_titolo, width=button_width)
        self.bottone_ordinare_titolo.pack(pady=5)

        self.bottone_ordinare_autore = tk.Button(self.bottoni_frame, text="Ordina per Autore", font=("Helvetica", 14), bg="#FF8C00", fg="white", command=self.ordina_per_autore, width=button_width)
        self.bottone_ordinare_autore.pack(pady=5)

        self.bottone_rimuovere = tk.Button(self.bottoni_frame, text="Rimuovi Libro", font=("Helvetica", 14), bg="#DC143C", fg="white", command=self.rimuovi_libro, width=button_width)
        self.bottone_rimuovere.pack(pady=5)

        self.bottone_prestare = tk.Button(self.bottoni_frame, text="Presta Libro", font=("Helvetica", 14), bg="#32CD32", fg="white", command=self.presta_libro, width=button_width)
        self.bottone_prestare.pack(pady=5)

        self.bottone_restituire = tk.Button(self.bottoni_frame, text="Restituisci Libro", font=("Helvetica", 14), bg="#8A2BE2", fg="white", command=self.restituisci_libro, width=button_width)
        self.bottone_restituire.pack(pady=5)

        self.bottone_ricerca = tk.Button(self.bottoni_frame, text="Cerca per Titolo", font=("Helvetica", 14), bg="#800080", fg="white", command=self.cerca_libro, width=button_width)
        self.bottone_ricerca.pack(pady=5)

    def aggiungi_libro(self):
        titolo = self.titolo_entry.get()
        autore = self.autore_entry.get()
        if titolo and autore:
            self.biblioteca.aggiungi_libro(titolo, autore)
            messagebox.showinfo("Successo", "Libro aggiunto con successo.")
        else:
            messagebox.showerror("Errore", "Titolo e autore devono essere compilati.")
        self.aggiorna_catalogo()

    def stampa_catalogo(self):
        self.aggiorna_catalogo()

    def ordina_per_titolo(self):
        self.biblioteca.ordina_per_titolo()
        self.aggiorna_catalogo()

    def ordina_per_autore(self):
        self.biblioteca.ordina_per_autore()
        self.aggiorna_catalogo()

    def rimuovi_libro(self):
        if not self.biblioteca.collezione:
            messagebox.showerror("Errore", "Il catalogo è vuoto.")
            return
        indice = simpledialog.askinteger("Rimuovi Libro", "Inserisci l'indice del libro da rimuovere (0-based):")
        if indice is not None:
            risultato = self.biblioteca.rimuovi_libro(indice)
            messagebox.showinfo("Risultato", risultato)
        self.aggiorna_catalogo()

    def presta_libro(self):
        if not self.biblioteca.collezione:
            messagebox.showerror("Errore", "Il catalogo è vuoto.")
            return
        indice = simpledialog.askinteger("Presta Libro", "Inserisci l'indice del libro da prestare (0-based):")
        if indice is not None:
            risultato = self.biblioteca.presta_libro(indice)
            messagebox.showinfo("Risultato", risultato)
        self.aggiorna_catalogo()

    def restituisci_libro(self):
        if not self.biblioteca.collezione:
            messagebox.showerror("Errore", "Il catalogo è vuoto.")
            return
        indice = simpledialog.askinteger("Restituisci Libro", "Inserisci l'indice del libro da restituire (0-based):")
        if indice is not None:
            risultato = self.biblioteca.restituisci_libro(indice)
            messagebox.showinfo("Risultato", risultato)
        self.aggiorna_catalogo()

    def cerca_libro(self):
        titolo = simpledialog.askstring("Cerca Libro", "Inserisci il titolo o parte del titolo da cercare:")
        if titolo:
            risultati = self.biblioteca.cerca_per_titolo(titolo)
            if risultati:
                risultati_testo = '\n'.join(str(libro) for libro in risultati)
                messagebox.showinfo("Risultati della Ricerca", risultati_testo)
            else:
                messagebox.showinfo("Risultati della Ricerca", "Nessun libro trovato.")

    def aggiorna_catalogo(self):
        catalogo = self.biblioteca.stampa_catalogo()
        self.catalogo_text.config(state=tk.NORMAL)
        self.catalogo_text.delete(1.0, tk.END)
        self.catalogo_text.insert(tk.END, catalogo if catalogo else "Il catalogo è vuoto.")
        self.catalogo_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfacciaGrafica(root)
    root.mainloop()
