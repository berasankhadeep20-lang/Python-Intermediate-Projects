#to create a file manager GUI application using tkinter and numpy in python and do the basic file operations
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import numpy as np
class FileManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("File Manager GUI")
        self.create_widgets()
        
    def create_widgets(self):
        self.open_button = tk.Button(self.master, text="Open File", command=self.open_file)
        self.open_button.pack(pady=10)
        
        self.save_button = tk.Button(self.master, text="Save File", command=self.save_file)
        self.save_button.pack(pady=10)
        
        self.delete_button = tk.Button(self.master, text="Delete File", command=self.delete_file)
        self.delete_button.pack(pady=10)
        
        self.file_content = tk.Text(self.master, wrap='word', width=60, height=20)
        self.file_content.pack(pady=10)
        
    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.file_content.delete(1.0, tk.END)
                self.file_content.insert(tk.END, content)
            messagebox.showinfo("File Opened", f"Opened file: {os.path.basename(file_path)}")
            
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            content = self.file_content.get(1.0, tk.END)
            with open(file_path, 'w') as file:
                file.write(content)
            messagebox.showinfo("File Saved", f"Saved file: {os.path.basename(file_path)}")
            
    def delete_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            os.remove(file_path)
            messagebox.showinfo("File Deleted", f"Deleted file: {os.path.basename(file_path)}")
            self.file_content.delete(1.0, tk.END)
if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerGUI(root)
    root.mainloop()