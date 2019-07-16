# -*- coding: utf-8 -*- 
import pyautogui
import time
from time import sleep
import keyboard

def MoveMouse(tensor):
    c1 = tuple(tensor[1:3].int()) #Top Left Coordinates
    c2 = tuple(tensor[3:5].int()) #Bottom Right Coordinates
    
    x1, y1 = int(c1[0].item()), int(c1[1].item())
    x2, y2 = int(c2[0].item()), int(c2[1].item())
     
    #Move Mouse to center of rectangle
    width = x2 -  x1
    height = y2 - y1 

    CenterX = x1 + int(width/2)
    CenterY =y1 + int(height/2)
    
    #pyautogui.moveTo(CenterX, CenterY)  
    #pyautogui.click(clicks=2) #Double click
    
    return 

def Fire(x, y, width, height):
    Ingame_Keybind_Fire = "k" #Ingame Keybind set to Fire(Not Mouse!!!)
    coordinates = pyautogui.position()
    x1, y1 = x, y
    x2, y2 = x+width, y+height
    CurrentX,CurrentY = coordinates[0], coordinates[1]
    print(coordinates)
    if (x1<CurrentX<x2) & (y1<CurrentY<y2): #Current mouse position is in rectangle
        #pyautogui.click(clicks=2) #Click
        keyboard.press(Ingame_Keybind_Fire) #Send the input to fire the weapon
        print("Press FIRE")
    return
