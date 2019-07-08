# -*- coding: utf-8 -*-
from __future__ import division
import torch 
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import cv2 

import os 
import os.path as osp

import CreateOverlay

def Rectangle(tensor):
    #RectanglePath = "C:/Users/micha/OneDrive/Desktop/Red.jpg"
    c1 = tuple(tensor[1:3].int()) #Top Left Coordinates
    c2 = tuple(tensor[3:5].int()) #Bottom Right Coordinates
    
    x1 = int(c1[0].item()) +175
    y1 = int(c1[1].item()) +133
    x2 = int(c2[0].item()) +175
    y2 = int(c2[1].item()) +133
     
    width = x2 -  x1
    height = y2 - y1 

    return width, height, x1, y1 #, RectanglePath

def run(tensor):
    #width, height, x, y,RectanglePath = Rectangle(tensor)
    width, height, x, y = Rectangle(tensor)
    #CreateOverlay.run(RectanglePath, width, height, x, y)
    CreateOverlay.run(width, height, x, y)
    return
