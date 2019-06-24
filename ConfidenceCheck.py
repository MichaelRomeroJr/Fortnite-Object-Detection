import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
from time import sleep

def run(tensor): #Only Display Object With Highest Confidence Score
    """TODO: Return only object with the second highest score """
    try:
        InitialConfidence = tensor[0][5].data.tolist()
        PrepReturnTensor = tensor[0]

        NumberofTensors = 0
        for t in tensor:
            CurrentConfidence = t[5].data.tolist()
            #print("CurrentConfidence: ", CurrentConfidence)
            if CurrentConfidence > InitialConfidence:
                PrepReturnTensor = t
                
            NumberofTensors+=1
        n = PrepReturnTensor.tolist() #Convert PrepReturnTensor tolist
        ReturnTensor = torch.Tensor([n]).cuda() #Create new 2D tensor with one entry, n
        return ReturnTensor

    except: #Multiple objects have not been detected
        print("Exception: ConfidenceCheck.run() error")
        return tensor


def score(tensor):
    try:
        confidence = tensor[5].data.tolist()
        return confidence
        
    except: #Multiple objects have not been detected
        print("Exception: ConfidenceCheck.score() error")
        return 0    
    
def SecondHighest(tensor): 
    NumberObjectsdDetected = len(tensor)
    if NumberObjectsdDetected > 1: #Multiple Objects
        try:
            InitialConfidence = tensor[0][5].data.tolist()
            PrepReturnTensor = tensor[0]

            NumberofTensors = 0
            for t in tensor:
                CurrentConfidence = t[5].data.tolist()
                #print("CurrentConfidence: ", CurrentConfidence)
                if CurrentConfidence > InitialConfidence:
                    PrepReturnTensor = t
                
                NumberofTensors+=1
            n = PrepReturnTensor.tolist() #Convert PrepReturnTensor tolist
            ReturnTensor = torch.Tensor([n]).cuda() #Create new 2D tensor with one entry, n
            return ReturnTensor

        except: #Multiple objects have not been detected
            print("Exception: ConfidenceCheck.run() error")
            return tensor
  
    return
