from __future__ import division
import torch 
from torch.autograd import Variable
from DarknetUtilities import util
from DarknetUtilities.util import *
import argparse
from darknet import Darknet
import time

from DarknetUtilities import TensorRefinement

from OperatingUtilities import StreamFromMonitor
from OperatingUtilities import Draw
from OperatingUtilities import Actions

def arg_parse():
    """Parse arguements to the detect module"""
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
CUDA = torch.cuda.is_available()

num_classes = 80
classes = load_classes("C:/Users/micha/data/coco.names")

#Set up the neural network 
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

def write(x, results):
    cls = int(x[-1])
    img = results
    ObjectedDetected = "{0}".format(classes[cls]) #label 
    
    if ObjectedDetected == 'person': 
        x, y, width, height = Draw.run(x)
        #Actions.Fire(x,y, width, height)
        #Actions.MoveMouse(x)

    return img

def Running():   
    start = time.time()
            
    try: 
        """StreamFromMonitor reads the moniitor saves it as an image than opens it up as a frame to work with"""
        start = time.time()
        frame = StreamFromMonitor.Stream()             
        img = prep_image(frame, inp_dim)
        im_dim = frame.shape[1], frame.shape[0]
        im_dim = torch.FloatTensor(im_dim).repeat(1,2)   
                     
        if CUDA:
            im_dim = im_dim.cuda()
            img = img.cuda()
        
        with torch.no_grad():
            output = model(Variable(img, volatile = True), CUDA)
            
        """output is tensor of all objects detected in image """
        output = write_results(output, confidence, num_classes, nms_thesh)
                
        """Pass output through functions to 
                first: remove all tensors that are not 'people'
                second: remove 'person at bottom of screen (probably self) """
        classes = load_classes('C:/Users/micha/data/coco.names')
        Output_People = TensorRefinement.DeterminePeople(output, classes)
        output = TensorRefinement.RemoveSelf(Output_People) 

        try:
            PeopleDetected = len(output)
            print("People (excluding self) detected: ", PeopleDetected)
        except:
            PeopleDetected = 0
                
        if PeopleDetected > 0:  #If anyone exlucding yourself is detected         
            im_dim = im_dim.repeat(output.size(0), 1)
            scaling_factor = torch.min(416/im_dim,1)[0].view(-1,1)
        
            output[:,[1,3]] -= (inp_dim - scaling_factor*im_dim[:,0].view(-1,1))/2
            output[:,[2,4]] -= (inp_dim - scaling_factor*im_dim[:,1].view(-1,1))/2
        
            output[:,1:5] /= scaling_factor

            for i in range(output.shape[0]):
                output[i, [1,3]] = torch.clamp(output[i, [1,3]], 0.0, im_dim[i,0])
                output[i, [2,4]] = torch.clamp(output[i, [2,4]], 0.0, im_dim[i,1])
    
            list(map(lambda x: write(x, frame), output))

            stop = time.time()
            duration = stop-start
            #print(duration)           
        
    except Exception as ex:
        print(type(ex), ex)
        #sys.exit()
        pass
    return
