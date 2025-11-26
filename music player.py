#to create a GUI music player using tkinter which plays audio files from the system
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import os
from collections import Counter
from PIL import Image, ImageTk
import cv2
import mediapipe as mp
import numpy as np
import time
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player with Hand Gesture Control")
        self.root.geometry("400x200")

        mixer.init()

        self.playlist = []
        self.current_index = 0

        self.load_button = tk.Button(root, text="Load Music", command=self.load_music)
        self.load_button.pack(pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.next_music)
        self.next_button.pack(pady=10)

        self.prev_button = tk.Button(root, text="Previous", command=self.prev_music)
        self.prev_button.pack(pady=10)

        self.cap = cv2.VideoCapture(0)
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils

        self.gesture_control()

    def load_music(self):
        files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3;*.wav")])
        self.playlist.extend(files)

    def play_music(self):
        if self.playlist:
            mixer.music.load(self.playlist[self.current_index])
            mixer.music.play()

    def next_music(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_music()

    def prev_music(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play_music()
    def gesture_control(self):
        ret, frame = self.cap.read()
        if not ret:
            self.root.after(100, self.gesture_control)
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)

        finger_count = 0
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger_count += self.count_fingers(hand_landmarks, frame.shape)
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

        if finger_count == 1:
            self.play_music()
        elif finger_count == 2:
            self.next_music()
        elif finger_count == 3:
            self.prev_music()

        cv2.imshow("Gesture Control", frame)
        cv2.waitKey(1)

        self.root.after(100, self.gesture_control)
    def count_fingers(self, hand_landmarks, image_shape):
        finger_tips_ids = [4, 8, 12, 16, 20]
        fingers_up = 0

        for tip_id in finger_tips_ids:
            tip_y = hand_landmarks.landmark[tip_id].y * image_shape[0]
            pip_y = hand_landmarks.landmark[tip_id - 2].y * image_shape[0]

            if tip_y < pip_y:
                fingers_up += 1

        return fingers_up
    
            
if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
    