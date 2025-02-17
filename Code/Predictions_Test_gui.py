import torch
import torchvision.transforms as transforms
from colorstuff.colorstuff import ColorResNet
from ColorNet import ColorNet
import numpy as np
import cv2
from line_profiler import LineProfiler
import time

from imutils.video import FileVideoStream
import argparse
import imutils

from multithreadimageload import InferenceDataStream, ColorCorrector

import psutil
import easygui
import os
import time

## Define function for gui sliders
def nothing(x):
	pass


	
##
## Read off arguments

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--profile", "-p", help="Run line profiling", action='store_true')
parser.add_argument("--demo", "-d", help="Puts the script into demo mode", action='store_true')
parser.add_argument("--cpu", "-c", help="Places the model on the cpu; runs calculations and inferences on cpu", action='store_true')
# read arguments from the command line
args = parser.parse_args()

torch.backends.cudnn.enabled == True

##
## Load the pytorch model and set video clip
if args.cpu:
	model= torch.load('../Models/ColorResNet_0_1_3.pt', map_location = 'cpu').eval().float()
else:
	model = torch.load('../Models/ColorResNet_0_1_3.pt').eval()
	

##
## Get video clip information
# ask the user for a video to demo via gui
video = easygui.fileopenbox()
if video is None:
	print('Failed to select a video')
	raise SystemExit(...)

# get video resolution information
vid = cv2.VideoCapture(video)
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('height is', height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print('width is', width)
vid.release()



##
## create the video and inference streams 
fvs = FileVideoStream(video, queue_size=30).start()
ivs = InferenceDataStream(fvs, model, queue_size=30, cpu=args.cpu).start()


##
## set up the color corrector
cc = ColorCorrector(model, intensity=0, cpu=args.cpu)

##
## The function for looping over the video
def livevideocorrection():

	desired_frames = 10000
	frame_number = 3000 # if not zero, specify res_override
	total_frames = desired_frames + frame_number
	last_time = time.monotonic()
	cv2.namedWindow('preview', cv2.WINDOW_NORMAL) # creates cv2 window entity called 'preview'
	cv2.resizeWindow('preview', (1280, 720)) # resizes cv2 window entitiy called 'preview'
	cv2.createTrackbar('Intensity', 'preview', 43,100, nothing)
	cv2.createTrackbar('Demoslider', 'preview', width//2, width, nothing)
	cv2.createTrackbar('Colorbox' , 'preview', 0,1,nothing)
	
	while ivs.more() and frame_number <= total_frames:
		
		#update intensity
		islider = cv2.getTrackbarPos('Intensity','preview')
		cc.intensity = islider/100
		
		#update demo slider
		dslider = cv2.getTrackbarPos('Demoslider','preview')
		cc.res_override = dslider
		
		# get corrected image
		
		prediction = (cc.predict(ivs.read(), frame_number, height, width, demo_mode = args.demo)*255).type(torch.uint8)
		
		

		# postprocess the image for display
		torch.cuda.synchronize()
		prediction = prediction.squeeze()
		prediction = prediction.detach()
		#prediction = prediction[[2,1,0],:,:]
		prediction = prediction.permute(1, 2, 0)
		prediction = prediction.cpu()
		prediction = prediction.numpy()
		prediction = cv2.cvtColor(prediction, cv2.COLOR_BGR2RGB) # Found to be smoother overall
		

		# print fps every ten frames
		if frame_number%10 == 0:
			current_time = time.monotonic()
			timedif = current_time - last_time
			FPS = 10/timedif
			print('FPS:' + str(FPS))
			last_time = time.monotonic()
		frame_number += 1

		# update the display
		bslider = cv2.getTrackbarPos('Colorbox','preview')
		cv2.putText(prediction, ('FPS: ' + str(FPS)),(width//2+20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
		# place color correct rectangle
		if bslider > 0:
			cv2.line(prediction,(0,80),(width,80),(51,103,246),25)
		
		if args.demo:
			cv2.line(prediction, (dslider ,0), (dslider, height), (255,255,255), 2)
			cv2.putText(prediction, ('Broadcasted'), ((dslider)-200, height-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			cv2.putText(prediction, ('Corrected'),((dslider+10),height-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
			
		key = cv2.waitKey(1) & 0xff
		
		# Pause feature
		
		if key==ord('p'):
			while True:
				key2 = cv2.waitKey(1) or 0xff
				cv2.imshow('preview',prediction)
				cv2.putText(prediction, 'Paused',(20,70), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 4)
				if key2 == ord('p'):
					last_time = time.monotonic()
					break
					
		cv2.imshow('preview',prediction)

		
	# clean up the environment
	cv2.destroyAllWindows()
	ivs.stop()
	fvs.stop()


if __name__=='__main__':
	
	if args.profile:
		lp = LineProfiler()
		lp.add_function(ColorCorrector.predict)
		lp_wrapper = lp(livevideocorrection)
		lp_wrapper()
		lp.print_stats()
	else:
		livevideocorrection()
	

	print('memory % used: '+ str(psutil.virtual_memory()[2]))






