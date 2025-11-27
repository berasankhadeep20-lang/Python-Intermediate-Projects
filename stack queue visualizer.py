#to visualize the implementation of stack queue data structures using tkinter
import tkinter as tk
from tkinter import messagebox
import random
import time
import threading
import sys
sys.setrecursionlimit(10**6)
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import heapq
import bisect
import collections
import queue
import copy
import math
import cmath
import itertools
import functools
import operator
import re
import json
import os
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("dequeue from empty queue")
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
class Visualizer:
    def __init__(self, data_structure):
        self.data_structure = data_structure
        self.root = tk.Tk()
        self.root.title("Data Structure Visualizer")
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="white")
        self.canvas.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.push_button = tk.Button(self.root, text="Push/Enqueue", command=self.push_enqueue)
        self.push_button.pack()
        self.pop_button = tk.Button(self.root, text="Pop/Dequeue", command=self.pop_dequeue)
        self.pop_button.pack()
        self.draw()
    def push_enqueue(self):
        value = self.entry.get()
        if value:
            if isinstance(self.data_structure, Stack):
                self.data_structure.push(value)
            elif isinstance(self.data_structure, Queue):
                self.data_structure.enqueue(value)
            self.entry.delete(0, tk.END)
            self.draw()
    def pop_dequeue(self):
        try:
            if isinstance(self.data_structure, Stack):
                self.data_structure.pop()
            elif isinstance(self.data_structure, Queue):
                self.data_structure.dequeue()
            self.draw()
        except IndexError as e:
            messagebox.showerror("Error", str(e))
    def draw(self):
        self.canvas.delete("all")
        items = self.data_structure.items
        for i, item in enumerate(items):
            x0 = 50 + i * 60
            y0 = 150
            x1 = x0 + 50
            y1 = y0 + 50
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="lightblue")
            self.canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=item)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    ds_type = input("Enter 'stack' to visualize Stack or 'queue' to visualize Queue: ").strip().lower()
    if ds_type == 'stack':
        data_structure = Stack()
    elif ds_type == 'queue':
        data_structure = Queue()
    else:
        print("Invalid input. Please enter 'stack' or 'queue'.")
        sys.exit(1)
    visualizer = Visualizer(data_structure)
    visualizer.run()
