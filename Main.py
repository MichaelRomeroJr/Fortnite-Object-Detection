# -*- coding: utf-8 -*-
import pyautogui
import time
from time import sleep
import pynput
from pynput import keyboard

import DetectWithCUDA

Going = True
while Going:
    DetectWithCUDA.Running()

def on_press(key):
    try: #alphanumeric key
        keypressed = key.char
        print("key: ", keypressed)
    except AttributeError: #special key
        keypressed = key
        print("key: w", keypressed)

    if keypressed == 'f': #print("You pressed F")
        print("Run AutoDetection")
        DetectWithCUDA.Running()

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc: # Stop listener    
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
