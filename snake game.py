#creating the hungry snake game using tkinter
import tkinter as tk
import random
from tkinter import messagebox
import numpy as np
class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.width = 400
        self.height = 400
        self.cell_size = 20
        self.direction = 'Right'
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.place_food()
        self.score = 0
        self.create_widgets()
        self.bind_keys()
        self.game_loop()
        
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg='black')
        self.canvas.pack()
        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=('Arial', 14))
        self.score_label.pack()
        
    def bind_keys(self):
        self.master.bind('<Up>', lambda event: self.change_direction('Up'))
        self.master.bind('<Down>', lambda event: self.change_direction('Down'))
        self.master.bind('<Left>', lambda event: self.change_direction('Left'))
        self.master.bind('<Right>', lambda event: self.change_direction('Right'))
        
    def change_direction(self, new_direction):
        opposite_directions = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
            
    def place_food(self):
        while True:
            x = random.randint(0, (self.width - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.height - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake:
                return (x, y)
                
    def game_loop(self):
        self.move_snake()
        if self.check_collisions():
            messagebox.showinfo("Game Over", f"Game Over! Your score: {self.score}")
            self.master.destroy()
            return
        if self.snake[0] == self.food:
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            self.food = self.place_food()
        else:
            self.snake.pop()
        self.draw_elements()
        self.master.after(100, self.game_loop)
        
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            new_head = (head_x, head_y - self.cell_size)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + self.cell_size)
        elif self.direction == 'Left':
            new_head = (head_x - self.cell_size, head_y)
        else:  # Right
            new_head = (head_x + self.cell_size, head_y)
        self.snake.insert(0, new_head)
    def check_collisions(self):
        head_x, head_y = self.snake[0]
        if (head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height):
            return True
        if self.snake[0] in self.snake[1:]:
            return True
        return False
    def draw_elements(self):
        self.canvas.delete("all")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill='green')
        food_x, food_y = self.food
        self.canvas.create_oval(food_x, food_y, food_x + self.cell_size, food_y + self.cell_size, fill='red')
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()