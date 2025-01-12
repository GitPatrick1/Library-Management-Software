#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Classe che rappresenta un libro
class Libro {
private:
    string titolo;
    string autore;
    bool inPrestito; // Indica se il libro è in prestito

public:
    // Costruttore per inizializzare un libro
    Libro(string t, string a) : titolo(t), autore(a), inPrestito(false) {}

    // Getter per ottenere il titolo del libro
    string getTitolo() {
        return titolo;
    }

    // Getter per ottenere l'autore del libro
    string getAutore() {
        return autore;
    }

    // Getter per sapere se il libro è in prestito
    bool getInPrestito() {
        return inPrestito;
    }

    // Setter per impostare lo stato "in prestito" del libro
    void setInPrestito(bool stato) {
        inPrestito = stato;
    }
};

// Classe che rappresenta una biblioteca
class Biblioteca {
private:
    vector<Libro> collezione; // Un vettore per memorizzare tutti i libri

public:
    // Aggiunge un nuovo libro alla collezione
    void aggiungiLibro(Libro libro) {
        collezione.push_back(libro); // Inserisce il libro alla fine del vettore
    }

    // Stampa l'elenco di tutti i libri
    void stampaCatalogo() {
        if (collezione.empty()) { // Verifica se il vettore è vuoto
            cout << "La biblioteca è vuota.\n";
        } else {
            cout << "Catalogo della biblioteca:\n";
            for (size_t i = 0; i < collezione.size(); i++) { // Itera su tutti gli elementi del vettore
                cout << i + 1 << ". Titolo: " << collezione[i].getTitolo()
                     << ", Autore: " << collezione[i].getAutore()
                     << ", In prestito: " << (collezione[i].getInPrestito() ? "Sì" : "No") << "\n";
            }
        }
    }

    // Cerca un libro per titolo
    void cercaPerTitolo(string titolo) {
        bool trovato = false;
        for (size_t i = 0; i < collezione.size(); i++) { // Itera su tutti gli elementi del vettore con indice
            if (collezione[i].getTitolo() == titolo) {
                cout << "Libro trovato: Titolo: " << collezione[i].getTitolo()
                     << ", Autore: " << collezione[i].getAutore()
                     << ", In prestito: " << (collezione[i].getInPrestito() ? "Sì" : "No") << "\n";
                trovato = true;
                break;
            }
        }
        if (!trovato) {
            cout << "Nessun libro trovato con il titolo \"" << titolo << "\".\n";
        }
    }

    // Rimuove un libro dal vettore dato un indice
    void rimuoviLibro(size_t indice) {
        if (indice == 0 || indice > collezione.size()) {
            cout << "Indice non valido.\n";
        } else {
            collezione.erase(collezione.begin() + (indice - 1)); // Rimuove l'elemento specifico
            cout << "Libro rimosso con successo.\n";
        }
    }

    // Ordina i libri per titolo usando un algoritmo semplice (bubble sort)
    void ordinaPerTitolo() {
        for (size_t i = 0; i < collezione.size(); i++) {
            for (size_t j = i + 1; j < collezione.size(); j++) {
                if (collezione[i].getTitolo() > collezione[j].getTitolo()) {
                    swap(collezione[i], collezione[j]); // Scambia due elementi nel vettore
                }
            }
        }
        cout << "Catalogo ordinato per titolo.\n";
    }

    // Ordina i libri per autore (stesso algoritmo di ordinamento)
    void ordinaPerAutore() {
        for (size_t i = 0; i < collezione.size(); i++) {
            for (size_t j = i + 1; j < collezione.size(); j++) {
                if (collezione[i].getAutore() > collezione[j].getAutore()) {
                    swap(collezione[i], collezione[j]);
                }
            }
        }
        cout << "Catalogo ordinato per autore.\n";
    }

    // Gestisce il prestito di un libro
    void prestaLibro(size_t indice) {
        if (indice == 0 || indice > collezione.size()) {
            cout << "Indice non valido.\n";
        } else if (collezione[indice - 1].getInPrestito()) {
            cout << "Il libro è già in prestito.\n";
        } else {
            collezione[indice - 1].setInPrestito(true); // Aggiorna lo stato del libro
            cout << "Libro prestato con successo.\n";
        }
    }

    // Gestisce la restituzione di un libro
    void restituisciLibro(size_t indice) {
        if (indice == 0 || indice > collezione.size()) {
            cout << "Indice non valido.\n";
        } else if (!collezione[indice - 1].getInPrestito()) {
            cout << "Il libro non è attualmente in prestito.\n";
        } else {
            collezione[indice - 1].setInPrestito(false);
            cout << "Libro restituito con successo.\n";
        }
    }
};

int main() {
    Biblioteca biblioteca; // Crea un'istanza della classe Biblioteca
    int scelta; // Variabile per memorizzare la scelta dell'utente

    do {
        // Menu principale
        cout << "\nGestione Biblioteca\n";
        cout << "1. Aggiungi libro\n";
        cout << "2. Stampa catalogo\n";
        cout << "3. Rimuovi libro\n";
        cout << "4. Ordina catalogo per titolo\n";
        cout << "5. Ordina catalogo per autore\n";
        cout << "6. Presta libro\n";
        cout << "7. Restituisci libro\n";
        cout << "8. Cerca libro per titolo\n";
        cout << "9. Esci\n";
        cout << "Scelta: ";
        cin >> scelta;

        switch (scelta) {
        case 1: {
            // Aggiunta di un nuovo libro
            cin.ignore(); // Per pulire il buffer di input
            string titolo, autore;
            cout << "Inserisci il titolo del libro: ";
            getline(cin, titolo);
            cout << "Inserisci l'autore del libro: ";
            getline(cin, autore);
            biblioteca.aggiungiLibro(Libro(titolo, autore));
            break;
        }
        case 2:
            // Stampa del catalogo
            biblioteca.stampaCatalogo();
            break;
        case 3: {
            // Rimozione di un libro
            size_t indice;
            cout << "Inserisci l'indice del libro da rimuovere: ";
            cin >> indice;
            biblioteca.rimuoviLibro(indice);
            break;
        }
        case 4:
            // Ordinamento per titolo
            biblioteca.ordinaPerTitolo();
            break;
        case 5:
            // Ordinamento per autore
            biblioteca.ordinaPerAutore();
            break;
        case 6: {
            // Prestito di un libro
            size_t indice;
            cout << "Inserisci l'indice del libro da prestare: ";
            cin >> indice;
            biblioteca.prestaLibro(indice);
            break;
        }
        case 7: {
            // Restituzione di un libro
            size_t indice;
            cout << "Inserisci l'indice del libro da restituire: ";
            cin >> indice;
            biblioteca.restituisciLibro(indice);
            break;
        }
        case 8: {
            // Ricerca di un libro per titolo
            cin.ignore();
            string titolo;
            cout << "Inserisci il titolo del libro da cercare: ";
            getline(cin, titolo);
            biblioteca.cercaPerTitolo(titolo);
            break;
        }
        case 9:
            // Uscita dal programma
            cout << "Uscita dal programma.\n";
            break;
        default:
            // Scelta non valida
            cout << "Scelta non valida. Riprova.\n";
        }
    } while (scelta != 9); // Ripete il menu finché l'utente non sceglie di uscire

    return 0; // Termine del programma
}
