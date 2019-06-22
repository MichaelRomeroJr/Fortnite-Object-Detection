import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np

""" Note: Returns the confidence score of the objected detected
          Omits first object detected since that's likely the user 
          since it's a first person shooter the game play view has the user in full view and is usually detected first. """
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np

def run(tensor):
    try: #Multiple objects have been detected
        InitialConfidence = tensor[0][5] #Confidence of initial objected detected
        
        PrepReturnTensor = tensor[0]

        NumberofTensors = 0
        for t in tensor: 
            #Iterate through each tensor. If confidence is higher than intial confedence then update return tensor
            CurrentConfidence = t[5]
    
            if CurrentConfidence > InitialConfidence:
                PrepReturnTensor = t
                
            NumberofTensors+=1
        n = PrepReturnTensor.tolist() #Convert PrepReturnTensor tolist
        ReturnTensor = torch.Tensor([n]) #Create new 2D tensor with one entry, n
           
        return ReturnTensor

    except: #One object detected
        print("Exception")
        return tensor

def score(tensor):
    try:
        score = tensor[0][5]
        return score.item()
    except:
        score = 0
        return score
