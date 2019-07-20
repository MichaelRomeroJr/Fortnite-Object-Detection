# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label): 
    "A Label that displays images, and plays them if they are gifs    :im: A PIL Image instance or a string filename"
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
            self.delay = 1
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

def run(width, height, x, y):
    root = tk.Tk()
    lbl = ImageLabel(root)
    lbl.pack()
    w, h = width, height
    
    imgpath = Image.new('RGB', (w, h), color = 'red') #Create Red Rectangle to overlay over target
    lbl.load(imgpath, w, h)
    
    label = lbl
    label.master.overrideredirect(True)
    GeometryString = "+" + str(x) + "+" + str(y)
    label.master.geometry(GeometryString) #label.master.geometry("+250+250")

    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    label.master.wm_attributes("-transparentcolor", "white")

    label.pack()
    
    root.after(25, root.destroy)  #root.after(1000, root.destroy)
    label.mainloop()
    
    return
