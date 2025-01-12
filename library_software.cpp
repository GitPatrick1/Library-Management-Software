#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Class representing a book
class Book {
private:
    string title;
    string author;
    bool isBorrowed; // Indicates if the book is borrowed

public:
    // Constructor to initialize a book
    Book(string t, string a) : title(t), author(a), isBorrowed(false) {}

    // Getter for the book's title
    string getTitle() {
        return title;
    }

    // Getter for the book's author
    string getAuthor() {
        return author;
    }

    // Getter to check if the book is borrowed
    bool getIsBorrowed() {
        return isBorrowed;
    }

    // Setter to update the "is borrowed" status of the book
    void setIsBorrowed(bool status) {
        isBorrowed = status;
    }
};

// Class representing a library
class Library {
private:
    vector<Book> collection; // A vector to store all books

public:
    // Adds a new book to the collection
    void addBook(Book book) {
        collection.push_back(book); // Adds the book to the end of the vector
    }

    // Prints the list of all books
    void printCatalog() {
        if (collection.empty()) { // Checks if the vector is empty
            cout << "The library is empty.\n";
        } else {
            cout << "Library catalog:\n";
            for (size_t i = 0; i < collection.size(); i++) { // Iterates through all elements in the vector
                cout << i + 1 << ". Title: " << collection[i].getTitle()
                     << ", Author: " << collection[i].getAuthor()
                     << ", Borrowed: " << (collection[i].getIsBorrowed() ? "Yes" : "No") << "\n";
            }
        }
    }

    // Searches for a book by title
    void searchByTitle(string title) {
        bool found = false;
        for (size_t i = 0; i < collection.size(); i++) { // Iterates through all elements in the vector
            if (collection[i].getTitle() == title) {
                cout << "Book found: Title: " << collection[i].getTitle()
                     << ", Author: " << collection[i].getAuthor()
                     << ", Borrowed: " << (collection[i].getIsBorrowed() ? "Yes" : "No") << "\n";
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "No book found with the title \"" << title << "\".\n";
        }
    }

    // Removes a book from the vector by index
    void removeBook(size_t index) {
        if (index == 0 || index > collection.size()) {
            cout << "Invalid index.\n";
        } else {
            collection.erase(collection.begin() + (index - 1)); // Removes the specified element
            cout << "Book successfully removed.\n";
        }
    }

    // Sorts books by title using a simple algorithm (bubble sort)
    void sortByTitle() {
        for (size_t i = 0; i < collection.size(); i++) {
            for (size_t j = i + 1; j < collection.size(); j++) {
                if (collection[i].getTitle() > collection[j].getTitle()) {
                    swap(collection[i], collection[j]); // Swaps two elements in the vector
                }
            }
        }
        cout << "Catalog sorted by title.\n";
    }

    // Sorts books by author (same sorting algorithm)
    void sortByAuthor() {
        for (size_t i = 0; i < collection.size(); i++) {
            for (size_t j = i + 1; j < collection.size(); j++) {
                if (collection[i].getAuthor() > collection[j].getAuthor()) {
                    swap(collection[i], collection[j]);
                }
            }
        }
        cout << "Catalog sorted by author.\n";
    }

    // Handles borrowing a book
    void borrowBook(size_t index) {
        if (index == 0 || index > collection.size()) {
            cout << "Invalid index.\n";
        } else if (collection[index - 1].getIsBorrowed()) {
            cout << "The book is already borrowed.\n";
        } else {
            collection[index - 1].setIsBorrowed(true); // Updates the book's status
            cout << "Book successfully borrowed.\n";
        }
    }

    // Handles returning a book
    void returnBook(size_t index) {
        if (index == 0 || index > collection.size()) {
            cout << "Invalid index.\n";
        } else if (!collection[index - 1].getIsBorrowed()) {
            cout << "The book is not currently borrowed.\n";
        } else {
            collection[index - 1].setIsBorrowed(false);
            cout << "Book successfully returned.\n";
        }
    }
};

int main() {
    Library library; // Creates an instance of the Library class
    int choice; // Variable to store the user's choice

    do {
        // Main menu
        cout << "\nLibrary Management\n";
        cout << "1. Add book\n";
        cout << "2. Print catalog\n";
        cout << "3. Remove book\n";
        cout << "4. Sort catalog by title\n";
        cout << "5. Sort catalog by author\n";
        cout << "6. Borrow book\n";
        cout << "7. Return book\n";
        cout << "8. Search book by title\n";
        cout << "9. Exit\n";
        cout << "Choice: ";
        cin >> choice;

        switch (choice) {
        case 1: {
            // Adding a new book
            cin.ignore(); // Clears the input buffer
            string title, author;
            cout << "Enter the book's title: ";
            getline(cin, title);
            cout << "Enter the book's author: ";
            getline(cin, author);
            library.addBook(Book(title, author));
            break;
        }
        case 2:
            // Printing the catalog
            library.printCatalog();
            break;
        case 3: {
            // Removing a book
            size_t index;
            cout << "Enter the index of the book to remove: ";
            cin >> index;
            library.removeBook(index);
            break;
        }
        case 4:
            // Sorting by title
            library.sortByTitle();
            break;
        case 5:
            // Sorting by author
            library.sortByAuthor();
            break;
        case 6: {
            // Borrowing a book
            size_t index;
            cout << "Enter the index of the book to borrow: ";
            cin >> index;
            library.borrowBook(index);
            break;
        }
        case 7: {
            // Returning a book
            size_t index;
            cout << "Enter the index of the book to return: ";
            cin >> index;
            library.returnBook(index);
            break;
        }
        case 8: {
            // Searching for a book by title
            cin.ignore();
            string title;
            cout << "Enter the title of the book to search for: ";
            getline(cin, title);
            library.searchByTitle(title);
            break;
        }
        case 9:
            // Exiting the program
            cout << "Exiting the program.\n";
            break;
        default:
            // Invalid choice
            cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 9); // Repeats the menu until the user chooses to exit

    return 0; // End of program
}
