import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np

""" Note: Returns the confidence score of the objected detected
          Omits first object detected since that's likely the user 
          since it's a first person shooter the game play view has the user in full view and is usually detected first.
    TODO: Not just choose the second most confident score, but ensure only the enemy is identified not the user """
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
