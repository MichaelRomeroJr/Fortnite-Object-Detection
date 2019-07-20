# -*- coding: utf-8 -*-
from OperatingUtilities import CreateOverlay

def Rectangle(tensor):
    """Input: tensor
        Output: Coordinates of object detected in tensor"""
    c1 = tuple(tensor[1:3].int()) #Top Left Coordinates
    c2 = tuple(tensor[3:5].int()) #Bottom Right Coordinates

    x1 = int(c1[0].item()) #+175
    y1 = int(c1[1].item()) #+133
    x2 = int(c2[0].item()) #+175
    y2 = int(c2[1].item()) #+133
     
    width = x2 -  x1
    height = y2 - y1 

    return width, height, x1, y1

def run(tensor):
    width, height, x, y = Rectangle(tensor) #Get Coordinates for rectangle to draw on screen
    CreateOverlay.run(width, height, x, y) #Draw rectangle on screen with the ability to click through it
    return x, y, width, height
