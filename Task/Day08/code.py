# Alarm Clock

import time
import datetime
import os
import pygame

pygame.mixer.init()

def play_alarm(sound_file):
    """Plays the alarm sound."""
    if os.path.exists(sound_file):  
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy(): 
            time.sleep(1)
    else:
        print(f"⚠ Error: Sound file '{sound_file}' not found!")

def set_alarms():
    alarms = []
    num_alarms = int(input("How many alarms do you want to set? "))

    for i in range(num_alarms):
        alarm_time = input(f"Enter alarm {i+1} time (HH:MM:SS): ").strip()
        sound_file = input(f"Enter sound file path for alarm {i+1} (or press Enter for default 'alarm.mp3'): ").strip()

        if not sound_file:  
            sound_file = r"C:\Users\ESHOP\Desktop\Python\Python Coding\Task\Day08\alarm.mp3"

        alarms.append((alarm_time, sound_file))

    print("\n⏳ Waiting for alarms...\n")

    while alarms:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        for alarm_time, sound_file in alarms[:]: 
            if current_time == alarm_time:
                print("\n⏰ Time's up! Wake up! 🔔")
                play_alarm(sound_file)

                snooze = input("Do you want to snooze? (yes/no): ").strip().lower()
                if snooze == "yes":
                    snooze_time = int(input("Enter snooze time in seconds: "))
                    time.sleep(snooze_time)
                    play_alarm(sound_file)

                alarms.remove((alarm_time, sound_file)) 

        time.sleep(1)

set_alarms()
