# -*- coding: utf-8 -*-
from PIL import ImageGrab
import numpy as np

def Stream():
    """Read entire monitor as a Pillow Image
        then convert to Numpy Array
        bbox specifies specific region (bbox= x,y,width,height)"""
    #img = ImageGrab.grab(bbox=(175,133,1750,950)) #Sample a smaller area of the monitor as Pil.Image
    img = ImageGrab.grab(bbox=(0,0,1920,1080) #Grab entire monitor as Pil.image
    img_np = np.array(img) 
    
    return img_np
