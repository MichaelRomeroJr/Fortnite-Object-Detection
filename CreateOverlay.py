# -*- coding: utf-8 -*-
"""Created on Thu Jun  6 19:09:56 2019 @author: micha"""
import numpy as np
import cv2
from time import sleep
import tkinter, win32api, win32con, pywintypes
from tkinter import *

import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

import tkinter as tk
import numpy as np
from PIL import Image, ImageTk

class ImageLabel(tk.Label): 
    "A Label that displays images, and plays them if they are gifs    :im: A PIL Image instance or a string filename"
    #def load(self, im):
    def load(self, im, width, height):
        if isinstance(im, str):
            im = Image.open(im)
            im = im.resize((width,height)) #Resize target box to  size of rectangle
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
        try:
            self.delay = im.info['duration']
        except:
            #self.delay = 100
            self.delay = 10
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
    def unload(self):
        self.config(image=None)
        self.frames = None
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

#def run(imgpath):
def run(imgpath, width, height, x, y):
    root = tk.Tk()
    lbl = ImageLabel(root)
    lbl.pack()
    w, h = width, height
    lbl.load(imgpath, w, h)
    
    label = lbl
    label.master.overrideredirect(True)
    GeometryString = "+" + str(x) + "+" + str(y)
    label.master.geometry(GeometryString)
    #label.master.geometry("+250+250")

    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "white")

    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))

    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    label.pack()
    #root.after(3000, root.destroy)
    root.after(50, root.destroy)
    label.mainloop()
    
    return
