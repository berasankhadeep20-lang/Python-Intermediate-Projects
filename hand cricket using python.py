#creating a hand cricket game using python and tkinter
import tkinter as tk
import random
from tkinter import messagebox
class HandCricketGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hand Cricket Game")
        self.player_score = 0
        self.computer_score = 0
        self.is_batting = True

        self.label = tk.Label(master, text="Welcome to Hand Cricket!", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.score_label = tk.Label(master, text="Player Score: 0 | Computer Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=10)

        self.instruction_label = tk.Label(master, text="Choose a number between 1 and 6:", font=("Helvetica", 12))
        self.instruction_label.pack(pady=10)

        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        for i in range(1, 7):
            button = tk.Button(self.buttons_frame, text=str(i), command=lambda i=i: self.play_round(i), width=4, height=2)
            button.grid(row=0, column=i-1, padx=5, pady=5)

    def play_round(self, player_choice):
        computer_choice = random.randint(1, 6)
        if self.is_batting:
            if player_choice == computer_choice:
                messagebox.showinfo("Out!", f"You chose {player_choice} and Computer chose {computer_choice}. You are out!")
                self.is_batting = False
                self.label.config(text="Computer's Turn to Bat!")
            else:
                self.player_score += player_choice
                messagebox.showinfo("Score!", f"You chose {player_choice} and Computer chose {computer_choice}. You scored {player_choice} runs!")
        else:
            if player_choice == computer_choice:
                messagebox.showinfo("Out!", f"You chose {player_choice} and Computer chose {computer_choice}. Computer is out!")
                self.end_game()
            else:
                self.computer_score += computer_choice
                messagebox.showinfo("Score!", f"You chose {player_choice} and Computer chose {computer_choice}. Computer scored {computer_choice} runs!")

        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Player Score: {self.player_score} | Computer Score: {self.computer_score}")

    def end_game(self):
        if self.player_score > self.computer_score:
            messagebox.showinfo("Game Over", f"You win! Final Score - Player: {self.player_score}, Computer: {self.computer_score}")
        elif self.player_score < self.computer_score:
            messagebox.showinfo("Game Over", f"Computer wins! Final Score - Player: {self.player_score}, Computer: {self.computer_score}")
        else:
            messagebox.showinfo("Game Over", f"It's a tie! Final Score - Player: {self.player_score}, Computer: {self.computer_score}")
        self.master.destroy()
if __name__ == "__main__":
    root = tk.Tk()
    game = HandCricketGame(root)
    root.mainloop()
