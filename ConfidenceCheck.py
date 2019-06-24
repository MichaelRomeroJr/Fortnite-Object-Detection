import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np

def run(tensor):
    try:
        InitialConfidence = tensor[0][5]
        
        PrepReturnTensor = tensor[0]
        
        print("InitialtConfidence: ", InitialConfidence)
        
        NumberofTensors = 0
        for t in tensor:
            CurrentConfidence = t[5]
            print("CurrentConfidence: ", CurrentConfidence)
            if CurrentConfidence > InitialConfidence:
                print("CurrentConfidence > InitialConfidence: ", CurrentConfidence > InitialConfidence)
                PrepReturnTensor = t
                
            NumberofTensors+=1
        n = PrepReturnTensor.tolist() #Convert PrepReturnTensor tolist
        ReturnTensor = torch.Tensor([n]) #Create new 2D tensor with one entry, n
           
        return ReturnTensor

    except: #Multiple objects have not been detected
        print("Exception: ConfidenceCheck.run() error")
        return tensor


def score(tensor):
    try:
        confidence = tensor[5]
        return confidence

    except: #Multiple objects have not been detected
        print("Exception: ConfidenceCheck.score() error")
        return 0    
