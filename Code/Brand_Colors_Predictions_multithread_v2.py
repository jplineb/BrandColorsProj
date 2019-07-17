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

torch.backends.cudnn.enabled == True

##
## Load the pytorch model and set video clip
if args.cpu:
	model= torch.load('../Models/ColorResNet_0_1_3.pt', map_location = 'cpu').eval().float()
else:
	model = torch.load('../Models/ColorResNet_0_1_3.pt').eval()
	

#video='FB-112418-USCClemson-Clip3_360p.mp4'
#video = 'clip2'
#video = 'Clip_2_trim.mp4'
#video = 'syracusetest.mp4'
video = 'Demo_Clip_576p_30.mp4'

##
## Get video clip resoultion information
vid = cv2.VideoCapture(video)
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('height is', height)
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print('width is', width)
vid.release()



##
## create the video and inference streams 
fvs = FileVideoStream(video, queue_size=15).start()
ivs = InferenceDataStream(fvs, model, queue_size=15, cpu=args.cpu).start()

##
## set up the color corrector
cc = ColorCorrector(model, intensity=float(args.intensity), cpu=args.cpu)

##
## The function for looping over the video
def livevideocorrection():

	desired_frames = 1000
	frame_number = 0 # if not zero, specify res_override
	total_frames = desired_frames + frame_number
	last_time = time.monotonic()
	#cv2.namedWindow('preview', cv2.WINDOW_NORMAL) # creates cv2 window entity called 'preview'
	#cv2.resizeWindow('preview', (1920, 1080)) # resizes cv2 window entitiy called 'preview'
	while ivs.more() and frame_number <= total_frames:
		
		# get corrected image
		prediction = (cc.predict(ivs.read(), frame_number, height, width, demo_mode = args.demo)*255).type(torch.uint8)
		
		
		

		# postprocess the image for display
		torch.cuda.synchronize()
		#rediction = prediction.float()
		#prediction = torch.nn.functional.interpolate(prediction, (1080, 1920), mode = 'area')
		prediction = prediction.squeeze()
		prediction = prediction.detach()
		prediction = prediction[[2,1,0],:,:]
		prediction = prediction.permute(1, 2, 0)
		prediction = prediction.cpu()
		prediction = prediction.numpy()
		#prediction = cv2.cvtColor(prediction, cv2.COLOR_BGR2RGB)

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
		cv2.putText(prediction, ('FPS: ' + str(FPS)),(width//2+20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
		
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



