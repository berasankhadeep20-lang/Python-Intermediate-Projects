#to create a working book library management system using tkinter and sqlite3
import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import simpledialog
class BookLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Library Management System")
        self.conn = sqlite3.connect('library.db')
        self.create_table()
        self.create_widgets()
        self.load_books()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        ''')
        self.conn.commit()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.listbox = tk.Listbox(self.frame, width=50, height=15)
        self.listbox.pack(side=tk.LEFT, padx=(0, 10))

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.add_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Book", command=self.delete_book)
        self.delete_button.pack(pady=5)

    def load_books(self):
        self.listbox.delete(0, tk.END)
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM books")
        for row in cursor.fetchall():
            self.listbox.insert(tk.END, f"{row[0]}: {row[1]} by {row[2]} ({row[3]})")

    def add_book(self):
        title = simpledialog.askstring("Input", "Enter book title:")
        author = simpledialog.askstring("Input", "Enter book author:")
        year = simpledialog.askinteger("Input", "Enter publication year:")

        if title and author and year:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
            self.conn.commit()
            self.load_books()
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

    def delete_book(self):
        selected = self.listbox.curselection()
        if selected:
            book_info = self.listbox.get(selected[0])
            book_id = int(book_info.split(":")[0])
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
            self.conn.commit()
            self.load_books()
        else:
            messagebox.showwarning("Selection Error", "No book selected!")
if __name__ == "__main__":
    root = tk.Tk()
    app = BookLibraryApp(root)
    root.mainloop()