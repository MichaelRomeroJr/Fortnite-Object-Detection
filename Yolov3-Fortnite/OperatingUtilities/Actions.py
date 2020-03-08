# -*- coding: utf-8 -*- 
import pyautogui

def Fire(x, y, width, height):
    """Fire when cursor is in displayed rectangle """
    coordinates = pyautogui.position()
    x1, y1 = x, y
    x2, y2 = x+width, y+height
         
    #Note: Fortnite cursor stays fixed in center of screen (the crosshairs)
    XCenter = 960.0
    YCenter = 540.0
    
    if (x1<XCenter<x2) & (y1<YCenter<y2): #Current mouse position is in rectangle
        print("Press Down")
        pyautogui.mouseDown() # does the same thing as a left-button mouse click
        sleep(1)
        pyautogui.mouseUp()
        print("Press Released")
      
    return
