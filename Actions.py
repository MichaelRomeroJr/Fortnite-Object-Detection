# -*- coding: utf-8 -*- 
import pyautogui
from time import sleep
import pynput
from pynput import keyboard

"""Import tensor that contains coordinates of drawn rectangles
    MoveMouse() moves the mouse to the center of the target box
     click() will result in firing in the middle of the rectangle
     TODO: Create function that will only fire in the center of the rectangle
          while a certain key is pressed. Otherwise, gameplay will be hard when 
          the cursor is constantly moving to rectangles being drawn"""

def MoveMouse(tensor):
    c1 = tuple(tensor[1:3].int()) #Top Left Coordinates
    c2 = tuple(tensor[3:5].int()) #Bottom Right Coordinates
    
    x1, y1 = int(c1[0].item()), int(c1[1].item())
    x2, y2 = int(c2[0].item()), int(c2[1].item())
     
    #Move Mouse to center of rectangle
    width = x2 -  x1
    height = y2 - y1 

    x = x1 + int(width/2)
    y =y1 + int(height/2)
    
    pyautogui.moveTo(x, y) #Move
    #pyautogui.click() #Click
    sleep(5)
    
    return 

def on_press(key):
    try: #alphanumeric key
        keypressed = key.char
        print("key: ", keypressed)
    except AttributeError: #special key
        keypressed = key
        print("key: ", keypressed)

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc: # Stop listener    
        return False

# Collect events until released
#with keyboard.Listener(on_press=on_press,
#        on_release=on_release) as listener:
#        listener.join()

# ...or, in a non-blocking fashion:
#listener = mouse.Listener( on_press=on_press, on_release=on_release)
#listener.start()

    

    
