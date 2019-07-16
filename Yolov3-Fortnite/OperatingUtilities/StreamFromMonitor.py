# -*- coding: utf-8 -*-
from PIL import ImageGrab
import numpy as np
import cv2
from time import sleep
from PIL import Image


def Stream():
    """Read entire monitor as a Pil.Image """
    #img = ImageGrab.grab(bbox=(10,10,1900,1000)) #bbox specifies specific region (bbox= x,y,width,height)
    """Sample a smaller area of the monitor"""
    img = ImageGrab.grab(bbox=(175,133,1750,950)) #bbox specifies specific region (bbox= x,y,width,height) 
    img_np = np.array(img) 
    #cv2.waitKey(1)
    
    return img_np


def run(path, framecount):
    #img = ImageGrab.grab(bbox=(100,100,190,100)) #bbox specifies specific region (bbox= x,y,width,height)
    img = ImageGrab.grab(bbox=(10,10,1900,1000)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img) 
    im = Image.fromarray(img_np)
    print(path + '/' + framecount + '.png')
    im.save(path + '/' + framecount + '.png') 
    cv2.waitKey(1)
    
    return
#cv2.destroyAllWindows()

    