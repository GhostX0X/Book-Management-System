import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


# Function to add a book to the XML file
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    genre = entry_genre.get()
    publication_year = entry_publication_year.get()

    if title and author and genre and publication_year:
        # Load the XML file
        tree = ET.parse('books.xml')
        root = tree.getroot()

        # Create a new book element
        book = ET.SubElement(root, 'book')

        # Add child elements for the book's attributes
        ET.SubElement(book, 'title').text = title
        ET.SubElement(book, 'author').text = author
        ET.SubElement(book, 'genre').text = genre
        ET.SubElement(book, 'publication_year').text = publication_year

        # Save the changes back to the XML file
        tree.write('books.xml')

        messagebox.showinfo("Success", "Book added successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

# Function to delete a book from the XML file
def delete_book():
    title = entry_title.get()

    if title:
        # Load the XML file
        tree = ET.parse('books.xml')
        root = tree.getroot()

        # Find the book with the given title and remove it
        for book in root.findall('book'):
            if book.find('title').text == title:
                root.remove(book)

        # Save the changes back to the XML file
        tree.write('books.xml')

        messagebox.showinfo("Success", "Book deleted successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please enter a title.")

# Function to search for books based on a given attribute value
def search_books():
    attribute = combo_attribute.get()
    value = entry_search.get()

    if attribute and value:
        # Load the XML file
        tree = ET.parse('books.xml')
        root = tree.getroot()

        # Find the books with the given attribute value
        books = []
        for book in root.findall('book'):
            if book.find(attribute).text == value:
                books.append(book)

        if books:
            result_text.delete(1.0, tk.END)
            for book in books:
                result_text.insert(tk.END, f"Title: {book.find('title').text}\n")
                result_text.insert(tk.END, f"Author: {book.find('author').text}\n")
                result_text.insert(tk.END, f"Genre: {book.find('genre').text}\n")
                result_text.insert(tk.END, f"Publication Year: {book.find('publication_year').text}\n")
                result_text.insert(tk.END, "----------------------------\n")
        else:
            messagebox.showinfo("No Results", "No books found with the given attribute value.")
    else:
        messagebox.showerror("Error", "Please select an attribute and enter a value.")

# Function to clear the entry fields
def clear_entries():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_genre.delete(0, tk.END)
    entry_publication_year.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Book Management")

# Create labels
label_title = tk.Label(window, text="Title:")
label_title.grid(row=0, column=0, sticky=tk.W)
label_author = tk.Label(window, text="Author:")
label_author.grid(row=1, column=0, sticky=tk.W)
label_genre = tk.Label(window, text="Genre:")
label_genre.grid(row=2, column=0, sticky=tk.W)
label_publication_year = tk.Label(window, text="Publication Year:")
label_publication_year.grid(row=3, column=0, sticky=tk.W)

# Create entry fields
entry_title = tk.Entry(window)
entry_title.grid(row=0, column=1)
entry_author = tk.Entry(window)
entry_author.grid(row=1, column=1)
entry_genre = tk.Entry(window)
entry_genre.grid(row=2, column=1)
entry_publication_year = tk.Entry(window)
entry_publication_year.grid(row=3, column=1)

# Create buttons
button_add = tk.Button(window, text="Add Book", command=add_book)
button_add.grid(row=4, column=0, pady=10)
button_delete = tk.Button(window, text="Delete Book", command=delete_book)
button_delete.grid(row=4, column=1)
button_search = tk.Button(window, text="Search Books", command=search_books)
button_search.grid(row=4, column=2)

# Create combobox for attribute selection
attributes = ['title', 'author', 'genre', 'publication_year']
combo_attribute = tk.ttk.Combobox(window, values=attributes)
combo_attribute.grid(row=5, column=0, padx=10, pady=10)

# Create entry field for search
entry_search = tk.Entry(window)
entry_search.grid(row=5, column=1)

# Create text area for search results
result_text = tk.Text(window, height=10, width=40)
result_text.grid(row=6, column=0, columnspan=3, padx=10)

# Run the main event loop
window.mainloop()
