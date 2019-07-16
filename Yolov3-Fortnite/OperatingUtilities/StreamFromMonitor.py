# -*- coding: utf-8 -*-
from PIL import ImageGrab
import numpy as np
from PIL import Image


def Stream():
    """Read entire monitor as a Pil.Image """
    #img = ImageGrab.grab(bbox=(10,10,1900,1000)) #bbox specifies specific region (bbox= x,y,width,height)
    """Sample a smaller area of the monitor as Pil.Image"""
    img = ImageGrab.grab(bbox=(175,133,1750,950)) #bbox specifies specific region (bbox= x,y,width,height) 
    img_np = np.array(img) 
    
    return img_np
