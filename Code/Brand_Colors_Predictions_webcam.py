import torch
import torchvision.transforms as transforms
from colorstuff.colorstuff import ColorResNet


import numpy as np
import cv2
from line_profiler import LineProfiler
import time


import argparse
import imutils

from multithreadimageload import InferenceDataStream, ColorCorrector, WebcamVideoStream


##
## Read off arguments

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--profile", "-p", help="Run line profiling", action='store_true')
parser.add_argument("--intensity", "-i", help="Scale factor for the correction mask", default=0.4)
parser.add_argument("--demo", "-d", help="Puts the script into demo mode", action='store_true')
parser.add_argument("--cpu", "-c", help="Places the model on the cpu; runs calculations and inferences on cpu", action='store_true')
# read arguments from the command line
args = parser.parse_args()


##
## Load the pytorch model and set video clip
if args.cpu:
	model= torch.load('../Models/ColorResNet_0_1_3.pt', map_location = 'cpu').eval().float()
else:
	model = torch.load('../Models/ColorResNet_0_1_3.pt').eval()
	
##
## Get video clip resoultion information
height = 360
width = 640




##
## create the video and inference streams 
fvs = WebcamVideoStream().start()
ivs = InferenceDataStream(fvs, model, queue_size=20, cpu=args.cpu).start()

##
## set up the color corrector
cc = ColorCorrector(model, intensity=float(args.intensity), cpu=args.cpu)

##
## The function for looping over the video
def livevideocorrection():
	last_time = time.monotonic()
	frame_number = 0
	cv2.namedWindow('preview', cv2.WINDOW_NORMAL) # creates cv2 window entity called 'preview'
	cv2.resizeWindow('preview', (1280, 720)) # resizes cv2 window entitiy called 'preview'
	while ivs.more():
		
		# get corrected image
		prediction = cc.predict(ivs.read(), frame_number, height, width, demo_mode = args.demo)
		
		# postprocess the image for display
		torch.cuda.synchronize()
		prediction = prediction.float()
		prediction = prediction.squeeze()
		prediction = prediction.detach()
		prediction = prediction[[2,1,0],:,:]
		prediction = prediction.permute(1, 2, 0)
		prediction = prediction.cpu()
		prediction = prediction.numpy()

		# print fps every ten frames
		if frame_number%10 == 0:
			current_time = time.monotonic()
			timedif = current_time - last_time
			FPS = 10/timedif
			print('FPS:' + str(FPS))
			last_time = time.monotonic()
		frame_number += 1

		# update the display
		cv2.putText(prediction, ('FPS: ' + str(int(FPS))),(height-30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
		
		if args.demo:
			cv2.line(prediction, (width//2 ,0), (width//2, height), (255,255,255), 2)
			cv2.putText(prediction, ('Broadcasted'), ((width//2)-200, height-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
			cv2.putText(prediction, ('Corrected'),((width//2+10),height-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
			
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



