import torch
import torchvision.transforms as transforms
from colorstuff.colorstuff import ColorResNet
import scipy
from PIL import Image
import numpy as np
import cv2
from line_profiler import LineProfiler
import time

from imutils.video import FileVideoStream
from imutils.video import FPS
import argparse
import imutils

from multithreadimageload import multithreadimageload

import psutil



###########  TESTING #####################

# Start the file video stream thread and allow the buffer to fill #
#print("[INFO] starting video file thread...")

#fvs = FileVideoStream('FB-112418-USCClemson-Clip13.mp4').start()
#time.sleep(1.0)

#while fvs.more():
	## grab the frame from the threaded video file stream, resize
	## it, and convert it to grayscale (while still retaining 3
	##channels)
	#frame = fvs.read()
	#frame = imutils.resize(frame, width=450)
	#frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#frame = np.dstack([frame, frame, frame])
 
	# display the size of the queue on the frame
	#cv2.putText(frame, "Queue Size: {}".format(fvs.Q.qsize()),
		#(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
 
	# show the frame and update the FPS counter
	#cv2.imshow("Frame", frame)
	#cv2.waitKey(1)

#cv2.destoryAllWindows()
#fvs.stop()


#####################################################################



def normalize(img):
    norm_img=img.clone().detach()
    norm_img[0]=(norm_img[0]-.485)/.229
    norm_img[1]=(norm_img[1]-.456)/.224
    norm_img[2]=(norm_img[2]-.406)/.225
  
    return norm_img



def predict_one(img, frame_number):
    #option 2
    #rgb_image = torch.tensor(img,dtype=torch.float16,device=torch.device('cuda:0'))
    alpha = multithreadimageload(img, queue_size = 25).start() # starts multithreadreadimageload
    rgb_image = alpha.read() # grabs the next frame from the queue
    #rgb_image = rgb_image.permute(2,0,1) #moved to multithread code
    #rgb_image = rgb_image/255 # moved to multithread code
    if frame_number%1 == 0 or frame_number <= 5:
    	normed=normalize(rgb_image)
    	normed=normed[None]
    	global prediction_orig
    	prediction_orig=model(normed)
    	prediction =(rgb_image + .4*(2*prediction_orig-1)).clamp(0,1)
    else:
    	prediction =(rgb_image + .4*(2*prediction_orig-1)).clamp(0,1)
    alpha.stop()
    return prediction

# read in a video file and display corrected version "on the fly"
def livevideocorrection(filepath, modelname):
	fvs = FileVideoStream(filepath, queue_size=128).start()
        # ivs = InferenceDataStream(fvs, queue_size=25).start() # --> inference video stream reads from file video stream and forms queue of prepped images for inference
	desired_frames = 250
	frame_number = 0
	last_time = time.monotonic()
	while fvs.more() and frame_number <= desired_frames:
		frame = fvs.read() # --> frame = ivs.read()
		if frame_number%10 == 0:
			current_time = time.monotonic()
			timedif = current_time - last_time
			FPS = 10/timedif
			print('FPS:' + str(FPS))
			last_time = time.monotonic()
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		prediction=(predict_one(frame, frame_number).squeeze().detach().cpu()) # --> prediction = predict_one(frame, frame_number) #why? because logic for preparing images is now done asyncronously in ivs.
		prediction=prediction.permute(1, 2, 0).numpy()
		prediction = cv2.cvtColor(prediction, cv2.COLOR_BGR2RGB)
		
		cv2.putText(prediction, "Queue Size: {}".format(fvs.Q.qsize()),
			(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
		cv2.putText(prediction, ('FPS: ' + str(FPS)),(750, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) 
		cv2.imshow('preview', prediction)
		frame_number += 1
		cv2.waitKey(1)
	
	cv2.destroyAllWindows()
	fvs.stop()

model= torch.load('../Models/ColorResNet_0_1.pt')
model.eval()

video='FB-112418-USCClemson-Clip3_360p.mp4'
#livevideocorrection(video, model)

lp = LineProfiler()
lp.add_function(predict_one)
lp_wrapper = lp(livevideocorrection)
lp_wrapper(video, model)
lp.print_stats()

print('memory % used: '+ str(psutil.virtual_memory()[2]))



