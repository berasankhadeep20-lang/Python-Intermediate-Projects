#to build a hangman game using tkinter
import tkinter as tk
import random
from tkinter import messagebox
import numpy as np
class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.words = ["python", "java", "kotlin", "javascript"]
        self.secret_word = random.choice(self.words)
        self.guessed_letters = set()
        self.attempts_left = 6
        self.create_widgets()
        self.update_display()
        
    def create_widgets(self):
        self.word_label = tk.Label(self.master, text="", font=('Arial', 24))
        self.word_label.pack(pady=20)
        
        self.entry = tk.Entry(self.master, font=('Arial', 16))
        self.entry.pack(pady=10)
        
        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)
        
        self.attempts_label = tk.Label(self.master, text=f"Attempts left: {self.attempts_left}", font=('Arial', 14))
        self.attempts_label.pack(pady=10)
        
    def update_display(self):
        display_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.secret_word])
        self.word_label.config(text=display_word)
        self.attempts_label.config(text=f"Attempts left: {self.attempts_left}")
        
    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        if guess in self.guessed_letters:
            messagebox.showinfo("Already Guessed", f"You already guessed '{guess}'.")
            return
        self.guessed_letters.add(guess)
        if guess not in self.secret_word:
            self.attempts_left -= 1
        self.update_display()
        self.check_game_over()
        
    def check_game_over(self):
        if all(letter in self.guessed_letters for letter in self.secret_word):
            messagebox.showinfo("Game Over", "Congratulations! You've guessed the word!")
            self.reset_game()
        elif self.attempts_left <= 0:
            messagebox.showinfo("Game Over", f"You've run out of attempts! The word was '{self.secret_word}'.")
            self.reset_game()
    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guessed_letters.clear()
        self.attempts_left = 6
        self.update_display()
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()