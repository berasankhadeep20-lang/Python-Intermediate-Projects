#to create a sudoko game using tkinter
import tkinter as tk
from tkinter import messagebox
import random
import time
import threading
import copy
class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Game")
        self.board = [[0]*9 for _ in range(9)]
        self.solution = [[0]*9 for _ in range(9)]
        self.selected_cell = None
        self.create_widgets()
        self.generate_board()
        self.start_time = time.time()
        self.timer_running = True
        threading.Thread(target=self.update_timer).start()
    def create_widgets(self):
        self.cells = {}
        for r in range(9):
            for c in range(9):
                entry = tk.Entry(self.master, width=2, font=('Arial', 24), justify='center')
                entry.grid(row=r, column=c, padx=1, pady=1)
                entry.bind("<FocusIn>", lambda e, row=r, col=c: self.select_cell(row, col))
                self.cells[(r, c)] = entry
        self.timer_label = tk.Label(self.master, text="Time: 0s", font=('Arial', 14))
        self.timer_label.grid(row=9, column=0, columnspan=9)
        self.check_button = tk.Button(self.master, text="Check Solution", command=self.check_solution)
        self.check_button.grid(row=10, column=0, columnspan=9)
    def generate_board(self):
        self.fill_board()
        self.solution = copy.deepcopy(self.board)
        self.remove_numbers()
        self.update_ui()
    def fill_board(self):
        def is_valid(num, row, col):
            for i in range(9):
                if self.board[row][i] == num or self.board[i][col] == num:
                    return False
            start_row, start_col = 3 * (row // 3), 3 * (col // 3)
            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    if self.board[r][c] == num:
                        return False
            return True
        def fill_cell(row, col):
            if row == 9:
                return True
            next_row, next_col = (row, col + 1) if col < 8 else (row + 1, 0)
            nums = list(range(1, 10))
            random.shuffle(nums)
            for num in nums:
                if is_valid(num, row, col):
                    self.board[row][col] = num
                    if fill_cell(next_row, next_col):
                        return True
                    self.board[row][col] = 0
            return False
        fill_cell(0, 0)
    def remove_numbers(self):
        attempts = 40
        while attempts > 0:
            r, c = random.randint(0, 8), random.randint(0, 8)
            if self.board[r][c] != 0:
                self.board[r][c] = 0
                attempts -= 1
    def update_ui(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] != 0:
                    self.cells[(r, c)].insert(0, str(self.board[r][c]))
                    self.cells[(r, c)].config(state='disabled')
                else:
                    self.cells[(r, c)].delete(0, tk.END)
                    self.cells[(r, c)].config(state='normal')
    def select_cell(self, row, col):
        self.selected_cell = (row, col)
    def check_solution(self):
        for r in range(9):
            for c in range(9):
                val = self.cells[(r, c)].get()
                if val == '' or int(val) != self.solution[r][c]:
                    messagebox.showinfo("Sudoku", "Incorrect Solution!")
                    return
        self.timer_running = False
        elapsed_time = int(time.time() - self.start_time)
        messagebox.showinfo("Sudoku", f"Congratulations! You solved it in {elapsed_time} seconds.")
    def update_timer(self):
        while self.timer_running:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"Time: {elapsed_time}s")
            time.sleep(1)
if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()