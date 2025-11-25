#creating the snake game using tkinter
import tkinter as tk
import numpy as np
class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.direction = "Down"
        self.draw_snake()
        self.master.bind("<Key>", self.change_direction)
        self.move_snake()
    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x+10, y+10, fill="green", tag="snake")
    def change_direction(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            self.direction = key
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - 10)
        elif self.direction == "Down":
            new_head = (head_x, head_y + 10)
        elif self.direction == "Left":
            new_head = (head_x - 10, head_y)
        elif self.direction == "Right":
            new_head = (head_x + 10, head_y)
        self.snake = [new_head] + self.snake[:-1]
        self.draw_snake()
        self.master.after(100, self.move_snake)
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()