import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["is_borrowed"])

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Borrowed: {'Yes' if self.is_borrowed else 'No'}"

class Library:
    def __init__(self):
        self.collection = []
        self.file_path = "catalog.json"
        self.load_catalog()

    def add_book(self, title, author):
        book = Book(title, author)
        self.collection.append(book)
        self.save_catalog()

    def print_catalog(self):
        return '\n'.join([str(book) for book in self.collection])

    def remove_book(self, index):
        if 0 <= index < len(self.collection):
            self.collection.pop(index)
            self.save_catalog()
            return "Book successfully removed."
        else:
            return "Invalid index."

    def sort_by_title(self):
        self.collection.sort(key=lambda x: x.title)
        self.save_catalog()
        return "Catalog sorted by title."

    def sort_by_author(self):
        self.collection.sort(key=lambda x: x.author)
        self.save_catalog()
        return "Catalog sorted by author."

    def borrow_book(self, index):
        if 0 <= index < len(self.collection):
            book = self.collection[index]
            if book.is_borrowed:
                return "The book is already borrowed."
            else:
                book.is_borrowed = True
                self.save_catalog()
                return "Book successfully borrowed."
        else:
            return "Invalid index."

    def return_book(self, index):
        if 0 <= index < len(self.collection):
            book = self.collection[index]
            if not book.is_borrowed:
                return "The book is not currently borrowed."
            else:
                book.is_borrowed = False
                self.save_catalog()
                return "Book successfully returned."
        else:
            return "Invalid index."

    def search_by_title(self, title):
        results = [book for book in self.collection if title.lower() in book.title.lower()]
        return results

    def save_catalog(self):
        with open(self.file_path, "w") as f:
            json.dump([book.to_dict() for book in self.collection], f)

    def load_catalog(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.collection = [Book.from_dict(item) for item in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.collection = []

class GUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management")
        self.root.geometry("1000x600")
        self.root.config(bg="#F4E1C1")

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, bg="#F4E1C1")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.catalog_frame = tk.Frame(self.main_frame, bg="#F4E1C1", width=600)
        self.catalog_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.title_label = tk.Label(self.catalog_frame, text="Library Management", font=("Helvetica", 24, "bold"), bg="#F4E1C1", fg="#8B4513")
        self.title_label.pack(pady=20)

        self.catalog_label = tk.Label(self.catalog_frame, text="Catalog:", font=("Helvetica", 16), bg="#F4E1C1", fg="#8B4513")
        self.catalog_label.pack()

        self.catalog_text = tk.Text(self.catalog_frame, width=70, height=15, wrap="word", font=("Helvetica", 12), bg="#FFF5E1", fg="#8B4513", state=tk.DISABLED)
        self.catalog_text.pack(pady=10)

        self.form_frame = tk.Frame(self.catalog_frame, bg="#F4E1C1")
        self.form_frame.pack(pady=10)

        self.title_label_form = tk.Label(self.form_frame, text="Title:", font=("Helvetica", 12), bg="#F4E1C1", fg="#8B4513")
        self.title_label_form.grid(row=0, column=0, padx=10)

        self.title_entry = tk.Entry(self.form_frame, font=("Helvetica", 12), bg="#FFF5E1", fg="#8B4513")
        self.title_entry.grid(row=0, column=1, padx=10)

        self.author_label_form = tk.Label(self.form_frame, text="Author:", font=("Helvetica", 12), bg="#F4E1C1", fg="#8B4513")
        self.author_label_form.grid(row=1, column=0, padx=10)

        self.author_entry = tk.Entry(self.form_frame, font=("Helvetica", 12), bg="#FFF5E1", fg="#8B4513")
        self.author_entry.grid(row=1, column=1, padx=10)

        self.buttons_frame = tk.Frame(self.main_frame, bg="#F4E1C1", width=400)
        self.buttons_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        button_width = 15

        self.add_button = tk.Button(self.buttons_frame, text="Add Book", font=("Helvetica", 14), bg="#228B22", fg="white", command=self.add_book, width=button_width)
        self.add_button.pack(pady=5)

        self.print_button = tk.Button(self.buttons_frame, text="Print Catalog", font=("Helvetica", 14), bg="#4682B4", fg="white", command=self.print_catalog, width=button_width)
        self.print_button.pack(pady=5)

        self.sort_title_button = tk.Button(self.buttons_frame, text="Sort by Title", font=("Helvetica", 14), bg="#FFD700", fg="white", command=self.sort_by_title, width=button_width)
        self.sort_title_button.pack(pady=5)

        self.sort_author_button = tk.Button(self.buttons_frame, text="Sort by Author", font=("Helvetica", 14), bg="#FF8C00", fg="white", command=self.sort_by_author, width=button_width)
        self.sort_author_button.pack(pady=5)

        self.remove_button = tk.Button(self.buttons_frame, text="Remove Book", font=("Helvetica", 14), bg="#DC143C", fg="white", command=self.remove_book, width=button_width)
        self.remove_button.pack(pady=5)

        self.borrow_button = tk.Button(self.buttons_frame, text="Borrow Book", font=("Helvetica", 14), bg="#32CD32", fg="white", command=self.borrow_book, width=button_width)
        self.borrow_button.pack(pady=5)

        self.return_button = tk.Button(self.buttons_frame, text="Return Book", font=("Helvetica", 14), bg="#8A2BE2", fg="white", command=self.return_book, width=button_width)
        self.return_button.pack(pady=5)

        self.search_button = tk.Button(self.buttons_frame, text="Search by Title", font=("Helvetica", 14), bg="#800080", fg="white", command=self.search_book, width=button_width)
        self.search_button.pack(pady=5)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.library.add_book(title, author)
            messagebox.showinfo("Success", "Book successfully added.")
        else:
            messagebox.showerror("Error", "Both title and author must be provided.")
        self.update_catalog()

    def print_catalog(self):
        self.update_catalog()

    def sort_by_title(self):
        self.library.sort_by_title()
        self.update_catalog()

    def sort_by_author(self):
        self.library.sort_by_author()
        self.update_catalog()

    def remove_book(self):
        if not self.library.collection:
            messagebox.showerror("Error", "The catalog is empty.")
            return
        index = simpledialog.askinteger("Remove Book", "Enter the index of the book to remove (0-based):")
        if index is not None:
            result = self.library.remove_book(index)
            messagebox.showinfo("Result", result)
        self.update_catalog()

    def borrow_book(self):
        if not self.library.collection:
            messagebox.showerror("Error", "The catalog is empty.")
            return
        index = simpledialog.askinteger("Borrow Book", "Enter the index of the book to borrow (0-based):")
        if index is not None:
            result = self.library.borrow_book(index)
            messagebox.showinfo("Result", result)
        self.update_catalog()

    def return_book(self):
        if not self.library.collection:
            messagebox.showerror("Error", "The catalog is empty.")
            return
        index = simpledialog.askinteger("Return Book", "Enter the index of the book to return (0-based):")
        if index is not None:
            result = self.library.return_book(index)
            messagebox.showinfo("Result", result)
        self.update_catalog()

    def search_book(self):
        title = simpledialog.askstring("Search Book", "Enter the title or part of the title to search for:")
        if title:
            results = self.library.search_by_title(title)
            if results:
                results_text = '\n'.join(str(book) for book in results)
                messagebox.showinfo("Search Results", results_text)
            else:
                messagebox.showinfo("Search Results", "No books found.")

    def update_catalog(self):
        catalog = self.library.print_catalog()
        self.catalog_text.config(state=tk.NORMAL)
        self.catalog_text.delete(1.0, tk.END)
        self.catalog_text.insert(tk.END, catalog if catalog else "The catalog is empty.")
        self.catalog_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
