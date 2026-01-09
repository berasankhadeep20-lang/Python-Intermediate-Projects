#to generate a to-do list from user input and set an alarm for a specific task at the specified time
import time
import threading
from datetime import datetime, timedelta
import winsound  # For Windows; use 'import os' and 'os.system("afplay /path/to/soundfile")' for macOS
import sys
import platform
import os
import subprocess
import shlex
def play_sound():
    if platform.system() == "Windows":
        duration = 1000  # milliseconds
        freq = 440  # Hz
        winsound.Beep(freq, duration)
    elif platform.system() == "Darwin":  # macOS
        os.system("afplay /System/Library/Sounds/Ping.aiff")
    else:  # Linux and others
        subprocess.call(shlex.split("aplay /usr/share/sounds/alsa/Front_Center.wav"))
def alarm_task(task_name, alarm_time):
    now = datetime.now()
    delay = (alarm_time - now).total_seconds()
    if delay > 0:
        time.sleep(delay)
    print(f"\nAlarm! Time to: {task_name}")
    play_sound()
def main():
    todo_list = []
    print("Welcome to the To-Do List with Alarm!")
    while True:
        task_name = input("Enter a task (or type 'done' to finish): ")
        if task_name.lower() == 'done':
            break
        alarm_input = input("Set an alarm for this task? (yes/no): ").strip().lower()
        alarm_time = None
        if alarm_input == 'yes':
            while True:
                time_input = input("Enter alarm time (HH:MM in 24-hour format): ")
                try:
                    now = datetime.now()
                    alarm_time = datetime.strptime(time_input, "%H:%M").replace(year=now.year, month=now.month, day=now.day)
                    if alarm_time < now:
                        alarm_time += timedelta(days=1)  # Set for next day if time has passed
                    break
                except ValueError:
                    print("Invalid time format. Please try again.")
        todo_list.append((task_name, alarm_time))
    print("\nYour To-Do List:")
    for idx, (task, alarm) in enumerate(todo_list, start=1):
        if alarm:
            print(f"{idx}. {task} - Alarm set for {alarm.strftime('%H:%M')}")
            threading.Thread(target=alarm_task, args=(task, alarm)).start()
        else:
            print(f"{idx}. {task} - No alarm set")
    print("You will be notified when it's time for your tasks with alarms.")
if __name__ == "__main__":
    main()
    