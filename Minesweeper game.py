#creating a minesweeper game using python and tkinter
import tkinter as tk
import random
from tkinter import messagebox
class MinesweeperGame:
    def __init__(self, master, size=8, mines=10):
        self.master = master
        self.master.title("Minesweeper Game")
        self.size = size
        self.mines = mines
        self.buttons = {}
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.game_over = False

        self.create_board()
        self.place_mines()
        self.calculate_numbers()

    def create_board(self):
        for r in range(self.size):
            for c in range(self.size):
                button = tk.Button(self.master, text="", width=3, height=1,
                                   command=lambda r=r, c=c: self.reveal_cell(r, c))
                button.bind("<Button-3>", lambda e, r=r, c=c: self.toggle_flag(r, c))
                button.grid(row=r, column=c)
                self.buttons[(r, c)] = button

    def place_mines(self):
        mine_positions = random.sample(range(self.size * self.size), self.mines)
        for pos in mine_positions:
            r, c = divmod(pos, self.size)
            self.board[r][c] = -1

    def calculate_numbers(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == -1:
                    continue
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.size and 0 <= nc < self.size and self.board[nr][nc] == -1:
                            count += 1
                self.board[r][c] = count

    def reveal_cell(self, r, c):
        if self.game_over or self.buttons[(r, c)].cget("text") == "F":
            return
        if self.board[r][c] == -1:
            self.buttons[(r, c)].config(text="*", bg="red")
            self.game_over = True
            messagebox.showinfo("Game Over", "You hit a mine! Game Over.")
            self.reveal_all_mines()
        else:
            self.buttons[(r, c)].config(text=str(self.board[r][c]), state="disabled", relief=tk.SUNKEN)
            if self.board[r][c] == 0:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < self.size and 0 <= nc < self.size:
                            self.reveal_cell(nr, nc)
        if self.check_win():
            self.game_over = True
            messagebox.showinfo("Congratulations", "You cleared the minefield!")
    def toggle_flag(self, r, c):
        if self.game_over or self.buttons[(r, c)].cget("state") == "disabled":
            return
        current_text = self.buttons[(r, c)].cget("text")
        if current_text == "F":
            self.buttons[(r, c)].config(text="")
        else:
            self.buttons[(r, c)].config(text="F")
    def reveal_all_mines(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] == -1:
                    self.buttons[(r, c)].config(text="*", bg="red")
    def check_win(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.board[r][c] != -1 and self.buttons[(r, c)].cget("state") != "disabled":
                    return False
        return True
if __name__ == "__main__":
    root = tk.Tk()
    game = MinesweeperGame(root)
    root.mainloop()