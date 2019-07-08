from __future__ import division
import torch 
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import cv2 
from util import *
import argparse
import os 
import os.path as osp
from darknet import Darknet
import pickle as pkl
import pandas as pd
import random
import time
from time import sleep
import ConfidenceCheck

import StreamFromMonitor

import Draw

###################################################################

def arg_parse():
    "    Parse arguements to the detect module"
    parser = argparse.ArgumentParser(description='YOLO v3 Detection Module')
    parser.add_argument("--bs", dest = "bs", help = "Batch size", default = 1)
    parser.add_argument("--confidence", dest = "confidence", help = "Object Confidence to filter predictions", default = 0.5)
    parser.add_argument("--nms_thresh", dest = "nms_thresh", help = "NMS Threshhold", default = 0.4)
    parser.add_argument("--cfg", dest = 'cfgfile', help = "Config file", default = "cfg/yolov3.cfg", type = str)
    parser.add_argument("--weights", dest = 'weightsfile', help = "weightsfile", default = "yolov3.weights", type = str)
    parser.add_argument("--reso", dest = 'reso', help =  "Input resolution of the network. Increase to increase accuracy. Decrease to increase speed", default = "416", type = str)
    parser.add_argument("--video", dest = "videofile", help = "Video file to     run detection on", default = "video.avi", type = str)
    return parser.parse_args()
    
args = arg_parse()
batch_size = int(args.bs)
confidence = float(args.confidence)
nms_thesh = float(args.nms_thresh)
start = 0
CUDA = torch.cuda.is_available()

num_classes = 80
classes = load_classes("C:/Users/micha/data/coco.names")

#Set up the neural network #print("Loading network.....")
model = Darknet(args.cfgfile)
model.load_weights(args.weightsfile) #print("Network successfully loaded")

model.net_info["height"] = args.reso
inp_dim = int(model.net_info["height"])
assert inp_dim % 32 == 0 
assert inp_dim > 32

#If there's a GPU availible, put the model on GPU
if CUDA:
    model.cuda()

#Set the model in evaluation mode
model.eval()

def write(x, results, confidencescore):
    #confidencescore = str(ConfidenceCheck.score(x))[7:]
    confidencescore = str(ConfidenceCheck.score(x))[:4]
    c1 = tuple(x[1:3].int())
    c2 = tuple(x[3:5].int())
    
    cls = int(x[-1])
    img = results
    label = "{0}".format(classes[cls]) # +' ' + score
    ObjectedDetected = label
    
    if ObjectedDetected == 'person': 
        
        #print("Object Detected: ", ObjectedDetected)
        Draw.run(x)
        #Actions.MoveMouse(x)
        pass
   
    # else :
   #     print("Object Detected: ", ObjectedDetected)
   #     print(type(ObjectedDetected))
    return img

#############################################################################

#####################################################################################

def Running():  
    
    frames = 0  
    start = time.time()
    RunningCount = 0

    while RunningCount < 1:
        #ret, frame = cap.read()
        ret = True
            
        if ret: 
            """StreamFromMonitor reads the moniitor saves it as an image than opens it up as a frame to work with"""
            start = time.time()
            frame = StreamFromMonitor.Stream() 
            
            img = prep_image(frame, inp_dim)

            #cv2.
            ("a", frame)
            im_dim = frame.shape[1], frame.shape[0]
            im_dim = torch.FloatTensor(im_dim).repeat(1,2)   
                     
            if CUDA:
                im_dim = im_dim.cuda()
                img = img.cuda()
        
            with torch.no_grad():
                output = model(Variable(img, volatile = True), CUDA)
            output = write_results(output, confidence, num_classes, nms_thesh)

            """Display object with highest confidence score"""
            try:
                ObjectsDetected = len(output)
            except:
                ObjectsDetected = 0
            
            if ObjectsDetected > 0: 
            #if ObjectsDetected > 1:
                #output = ConfidenceCheck.run(output)
                #output = ConfidenceCheck.SecondHighest(output)
                #confidencescore = ConfidenceCheck.score(output)
                confidencescore = 0
            
                if type(output) == int:
                    frames += 1
                                   
                    key = cv2.waitKey(1)
                    if key & 0xFF == ord('q'):
                        break
                    continue
        
                im_dim = im_dim.repeat(output.size(0), 1)
                scaling_factor = torch.min(416/im_dim,1)[0].view(-1,1)
        
                output[:,[1,3]] -= (inp_dim - scaling_factor*im_dim[:,0].view(-1,1))/2
                output[:,[2,4]] -= (inp_dim - scaling_factor*im_dim[:,1].view(-1,1))/2
        
                output[:,1:5] /= scaling_factor

                for i in range(output.shape[0]):
                    output[i, [1,3]] = torch.clamp(output[i, [1,3]], 0.0, im_dim[i,0])
                    output[i, [2,4]] = torch.clamp(output[i, [2,4]], 0.0, im_dim[i,1])
    
                classes = load_classes('C:/Users/micha/data/coco.names')
                colors = pkl.load(open("pallete", "rb"))
            
                
                list(map(lambda x: write(x, frame, confidencescore), output))
            
                """Display the image with drawn rectangles"""
                #cv2.imshow("frame", frame)
                                 
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'): #print("'if key & 0xFF == ord('q')' break")
                    break
                frames += 1

                stop = time.time()
                duration = stop-start
                #print(duration)
            
            if ObjectsDetected == 1:
                pass
            else:
                pass #break
        RunningCount+=1    
        
    else: #Frames we want to skip #print('ERROR: thingy = False')
        return
        
    
    return
