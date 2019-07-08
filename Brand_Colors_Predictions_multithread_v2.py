import torch
import torchvision.transforms as transforms
from colorstuff.colorstuff import ColorResNet
from PIL import Image
import numpy as np
import cv2
from line_profiler import LineProfiler
import time

from imutils.video import FileVideoStream
import argparse
import imutils

from multithreadimageload import InferenceDataStream, ColorCorrector

import psutil

##
## Read off arguments

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--profile", "-p", help="Run line profiling", action='store_true')
parser.add_argument("--intensity", "-i", help="Scale factor for the correction mask", default=0.4)

# read arguments from the command line
args = parser.parse_args()


##
## Load the pytorch model and set video clip
model= torch.load('../Models/ColorResNet_0_1_3.pt').eval()
#video='FB-112418-USCClemson-Clip3_360p.mp4'
video = 'clip2'


##
## create the video and inference streams 
fvs = FileVideoStream(video, queue_size=15).start()
ivs = InferenceDataStream(fvs, model, queue_size=15).start()

##
## set up the color corrector
cc = ColorCorrector(model, intensity=float(args.intensity))

##
## The function for looping over the video
def livevideocorrection():

	desired_frames = 2000
	frame_number = 0
	last_time = time.monotonic()
	#cv2.namedWindow('preview', cv2.WINDOW_NORMAL) # creates cv2 window entity called 'preview'
	#cv2.resizeWindow('preview', (1920, 1080)) # resizes cv2 window entitiy called 'preview'
	while ivs.more() and frame_number <= desired_frames:
		
		# get corrected image
		prediction = cc.predict(ivs.read(), frame_number)

		# postprocess the image for display
		prediction = prediction.float()
		prediction = prediction.squeeze()
		prediction = prediction.detach()
		prediction = prediction.permute(1, 2, 0)
		prediction = prediction.cpu()
		prediction = prediction.numpy()
		prediction = cv2.cvtColor(prediction, cv2.COLOR_BGR2RGB)

		# print fps every ten frames
		if frame_number%10 == 0:
			current_time = time.monotonic()
			timedif = current_time - last_time
			FPS = 10/timedif
			print('FPS:' + str(FPS))
			last_time = time.monotonic()
		frame_number += 1

		# update the display
		cv2.putText(prediction, "Queue Size (FVS/IVS): {}/{}".format(fvs.Q.qsize(), ivs.Q.qsize()),
			(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
		cv2.putText(prediction, ('FPS: ' + str(FPS)),(750, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) 
		cv2.imshow('preview', prediction)
		cv2.waitKey(1)
		

		
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



