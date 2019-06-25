import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
from time import sleep
import time

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
        #print("Exception: ConfidenceCheck.run() error")
        return tensor

def score(tensor):
    try:
        confidence = tensor[5].data.tolist()
        return confidence
        
    except: #Multiple objects have not been detected
        print("Exception: ConfidenceCheck.score() error")
        return 0    
    
def SecondHighest(tensor): 
    try:
        NumberObjectsdDetected = len(tensor)
        ListOfTensors = []
        if NumberObjectsdDetected > 1: #Multiple Objects
            for i in range(NumberObjectsdDetected):
                ListOfTensors.append(tensor[i].tolist())
        
            ListOfTensorsSorted = sorted(ListOfTensors, key=lambda x: x[5], reverse=True)

            for i in ListOfTensorsSorted:
                pass
        
            SecondHighestList = ListOfTensorsSorted[1]  
            ReturnTensor = torch.Tensor([SecondHighestList]).cuda()
        
        else: #One Object Detected
            ReturnTensor = tensor
        
        return ReturnTensor
    except:
        print("Exception")
        return tensor
    
