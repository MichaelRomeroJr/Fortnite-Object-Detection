import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np


def run(tensor):
    try:
        Object2 = tensor[1] #Get Second Object Detected
        n = Object2.tolist() #Convert tensor tolist
        x = torch.Tensor([n]) #Create new 2D tensor with one entry, n
        return x
    except: #Multiple objects have not been detected
        print("Exception")
        return tensor

def score(tensor):
    try:
        score = tensor[0][5]
        return score.item()
    except:
        score = 0
        return score