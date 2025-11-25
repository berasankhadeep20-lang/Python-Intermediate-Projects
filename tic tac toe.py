#to create a tic tac toe game vs the cpu using tkinter
import tkinter as tk
import random
from tkinter import messagebox
import numpy as np
import time
class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = np.zeros((3, 3), dtype=int)
        self.current_player = 1  # 1 for player, -1 for CPU
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
        
    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text="", font=('Arial', 60), width=5, height=2,
                                   command=lambda row=i, col=j: self.player_move(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
                
    def player_move(self, row, col):
        if self.board[row][col] == 0 and self.current_player == 1:
            self.board[row][col] = 1
            self.buttons[row][col].config(text="X", state="disabled")
            if self.check_winner(1):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_game()
            elif np.all(self.board != 0):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = -1
                self.master.after(500, self.cpu_move)
                
    def cpu_move(self):
        empty_cells = np.argwhere(self.board == 0)
        if empty_cells.size > 0:
            choice = random.choice(empty_cells)
            row, col = choice
            self.board[row][col] = -1
            self.buttons[row][col].config(text="O", state="disabled")
            if self.check_winner(-1):
                messagebox.showinfo("Game Over", "CPU wins!")
                self.reset_game()
            elif np.all(self.board != 0):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = 1
                
    def check_winner(self, player):
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
