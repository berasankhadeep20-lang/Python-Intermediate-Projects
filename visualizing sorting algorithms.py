#to visualize the sorting algorithms using tkinter
import tkinter as tk
import random
import time
import threading
import sys
from tkinter import messagebox
import importlib.util
# Check if matplotlib is installed
spec = importlib.util.find_spec("matplotlib")
if spec is None:
    print("The 'matplotlib' library is required to run this program.")
    print("Please install it using 'pip install matplotlib' and try again.")
    sys.exit(1)
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import numpy as np
class SortingVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting Algorithm Visualizer")
        self.array = []
        self.algorithm = tk.StringVar(value="Bubble Sort")
        self.is_sorting = False

        # UI Elements
        self.create_widgets()
        self.setup_plot()

    def create_widgets(self):
        control_frame = tk.Frame(self.master)
        control_frame.pack(side=tk.TOP, fill=tk.X)

        tk.Label(control_frame, text="Algorithm:").pack(side=tk.LEFT, padx=5)
        algo_menu = tk.OptionMenu(control_frame, self.algorithm, "Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort")
        algo_menu.pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="Generate Array", command=self.generate_array).pack(side=tk.LEFT, padx=5)
        tk.Button(control_frame, text="Start Sorting", command=self.start_sorting).pack(side=tk.LEFT, padx=5)

    def setup_plot(self):
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def generate_array(self):
        if self.is_sorting:
            messagebox.showwarning("Warning", "Cannot generate a new array while sorting!")
            return
        self.array = [random.randint(1, 100) for _ in range(50)]
        self.draw_array()

    def draw_array(self, highlight_indices=None):
        self.ax.clear()
        bar_colors = ['blue'] * len(self.array)
        if highlight_indices:
            for index in highlight_indices:
                bar_colors[index] = 'red'
        self.ax.bar(range(len(self.array)), self.array, color=bar_colors)
        self.ax.set_title(f"{self.algorithm.get()} Visualization")
        self.canvas.draw()

    def start_sorting(self):
        if not self.array:
            messagebox.showwarning("Warning", "Please generate an array first!")
            return
        if self.is_sorting:
            messagebox.showwarning("Warning", "Sorting is already in progress!")
            return
        self.is_sorting = True
        threading.Thread(target=self.sort_array).start()

    def sort_array(self):
        algorithm = self.algorithm.get()
        if algorithm == "Bubble Sort":
            self.bubble_sort()
        elif algorithm == "Selection Sort":
            self.selection_sort()
        elif algorithm == "Insertion Sort":
            self.insertion_sort()
        elif algorithm == "Merge Sort":
            self.merge_sort(0, len(self.array) - 1)
        elif algorithm == "Quick Sort":
            self.quick_sort(0, len(self.array) - 1)
        self.is_sorting = False
        self.draw_array()
    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                self.draw_array(highlight_indices=[j, j+1])
                time.sleep(0.05)
    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
                self.draw_array(highlight_indices=[i, j])
                time.sleep(0.05)
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
    def insertion_sort(self):
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i-1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
                self.draw_array(highlight_indices=[j, j+1])
                time.sleep(0.05)
            self.array[j + 1] = key
    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)
    def merge(self, left, mid, right):
        L = self.array[left:mid + 1]
        R = self.array[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                self.array[k] = L[i]
                i += 1
            else:
                self.array[k] = R[j]
                j += 1
            self.draw_array(highlight_indices=[k])
            time.sleep(0.05)
            k += 1
        while i < len(L):
            self.array[k] = L[i]
            self.draw_array(highlight_indices=[k])
            time.sleep(0.05)
            i += 1
            k += 1
        while j < len(R):
            self.array[k] = R[j]
            self.draw_array(highlight_indices=[k])
            time.sleep(0.05)
            j += 1
            k += 1
    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)
    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
            self.draw_array(highlight_indices=[i, j])
            time.sleep(0.05)
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1
if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()