#to develop a contact book application using Python and Tkinter and save the contacts in a CSV file.
import tkinter as tk
import numpy as np
class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")
        self.contacts = []
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(master)
        self.name_entry.pack()
        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(master)
        self.phone_entry.pack()
        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.pack()
        self.save_button = tk.Button(master, text="Save Contacts", command=self.save_contacts)
        self.save_button.pack()
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            self.contacts.append((name, phone))
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
    def save_contacts(self):
        with open("contacts.csv", "w") as f:
            for name, phone in self.contacts:
                f.write(f"{name},{phone}\n")
if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()