from threading import Thread
import sys
import torch
import torchvision.transforms as transforms
import time
import cv2
from queue import Queue

class ColorCorrector:
	
	#class members
	#norm_mu = torch.tensor([0.485, 0.456, 0.406], dtype=torch.float16,device=torch.device('cuda:0')).reshape(3,1,1)
	#norm_sd = torch.tensor([0.229, 0.224, 0.225], dtype=torch.float16,device=torch.device('cuda:0')).reshape(3,1,1)
	
	def __init__(self, model, intensity=0.4, cpu=False, res_override = None):
		self.model=model
		self.intensity=intensity
		self.res_override = res_override
		# class members
		
		if cpu:
			self.norm_mu = (torch.tensor([0.485, 0.456, 0.406], dtype=torch.float32)).reshape(3,1,1)
			self.norm_sd = (torch.tensor([0.229, 0.224, 0.225], dtype=torch.float32)).reshape(3,1,1)
		else:
			self.norm_mu = torch.tensor([0.485, 0.456, 0.406], dtype=torch.float16,device=torch.device('cuda:0')).reshape(3,1,1)
			self.norm_sd = torch.tensor([0.229, 0.224, 0.225], dtype=torch.float16,device=torch.device('cuda:0')).reshape(3,1,1)
		
	 
	def predict(self, rgb_image, frame_number, video_height, video_width, demo_mode = False):
		if self.res_override is not None:
			self.x1 = 0
			self.x2 = self.res_override
			#self.x2 = res_override[0]//2
			#self.y1 = 0
			#self.y2 = res_override[1]//2
			
		else:
			self.x1 = 0
			self.x2 = video_width//2
			self.y1 = 0
			self.y2 = video_height//2
			#outdated
			#else:
				#imgsize = rgb_image.size()
				#self.x1 = 0
				#self.x2 = imgsize[2]//2
				#self.y1 = 0
				#self.y2 = imgsize[1]//2
			


		if frame_number%1 == 0 or frame_number <= 5:
			img_normed = self._normalize(rgb_image)[None]
			self.prediction_orig = self.model(img_normed)

		
		prediction =rgb_image + self.intensity*2.0*self.prediction_orig-self.intensity
		
		if demo_mode:
			uncorrected = rgb_image.unsqueeze(0) # Generates the uncorrected section
			prediction[:,:,:,self.x1:self.x2] = uncorrected[:,:,:,self.x1:self.x2] # Adds uncorrected section back onto the corrected mask
		

		return prediction.clamp(0,1)
		
	def _normalize(self, img):
		norm_img=img.clone().detach()
		return (norm_img - self.norm_mu)/self.norm_sd

class InferenceDataStream:
	
	def __init__(self, fvs, model, transforms=None, queue_size=25, cpu=False):
		
		# initialize the process
		self.stream = fvs
		self.model = model
		self.stopped = False
		self.transfrom = transforms
		self.cpu = cpu
		# Initialize the Queue
		self.Q = Queue(maxsize=queue_size)
		# initialize thread
		self.thread = Thread(target=self.update, args=())
		self.thread.daemon = True

		self.tries=0
		
	def start(self):
		# start a thread to load tensors onto gpu from frames
		self.thread.start()
		return self
		
	def update(self):
		#keep looping infinitely
		while True:
			# keep track of the number of frames
			
			if self.stopped:
				break
			
			# if Q is not full read another into it
			if not self.Q.full():
				# read from file stream
				img = self.stream.read()
				# change colors
				#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				
				# format tensor type
				cpu = self.cpu
				if cpu:
					frame = torch.tensor(img,dtype=torch.float32).permute(2,0,1)/255
				else:
					frame = torch.tensor(img,dtype=torch.float16,device=torch.device('cuda:0')).permute(2,0,1)/255
					frame = frame[[2,1,0],:,:]


				self.Q.put(frame) # adds frame to the queue
				
			else:
				time.sleep(0.2) #rest for 10ms, we have a full queue
		
	def read(self):
		# returns next frame to load in the queue
		return self.Q.get()
		
	def running(self):
		return self.more() or not self.stopped
		
	def more(self):
		#returns True if there are still frames to be loaded
		while self.Q.qsize() == 0 and not self.stopped and self.tries < 5:
			time.sleep(0.1)
			self.tries += 1

		self.tries=0
	
		return self.Q.qsize() > 0 
		
	def stop(self):
		# inidcate that the thread should be stopped
		self.stopped = True
		# wait until stream resource are released
		#self.thread.join()
		
#################################################################		
class WebcamVideoStream:
	def __init__(self, src=0, name="WebcamVideoStream"):
		# initialize the video camera stream and read the first frame
		# from the stream
		self.stream = cv2.VideoCapture(src)
		self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, 620)
		self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
		(self.grabbed, self.frame) = self.stream.read()

		# initialize the thread name
		self.name = name

		# initialize the variable used to indicate if the thread should
		# be stopped
		self.stopped = False

	def start(self):
		# start the thread to read frames from the video stream
		t = Thread(target=self.update, name=self.name, args=())
		t.daemon = True
		t.start()
		return self

	def update(self):
		# keep looping infinitely until the thread is stopped
		while True:
			# if the thread indicator variable is set, stop the thread
			if self.stopped:
				return

			# otherwise, read the next frame from the stream
			(self.grabbed, self.frame) = self.stream.read()

	def read(self):
		# return the frame most recently read
		return self.frame

	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True		

###############################################################
class InferenceDataStreamRT:
	
	def __init__(self, fvs, transforms=None, queue_size=25, cpu=False):
		
		# initialize the process
		self.stream = fvs
		self.stopped = False
		self.transfrom = transforms
		self.cpu = cpu
		# Initialize the Queue
		self.Q = Queue(maxsize=queue_size)
		# initialize thread
		self.thread = Thread(target=self.update, args=())
		self.thread.daemon = True

		self.tries=0
		
	def start(self):
		# start a thread to load tensors onto gpu from frames
		self.thread.start()
		return self
		
	def update(self):
		#keep looping infinitely
		while True:
			# keep track of the number of frames
			
			if self.stopped:
				break
			
			# if Q is not full read another into it
			if not self.Q.full():
				# read from file stream
				img = self.stream.read()
				# change colors
				imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				# format tensor type
				norm_img = imgS.copy()
				norm_img = norm_img.transpose([2, 0, 1])/255
				norm_img[0]=(norm_img[0]-.485)/.229
				norm_img[1]=(norm_img[1]-.456)/.224
				norm_img[2]=(norm_img[2]-.406)/.225
				
				
			

				self.Q.put([norm_img, img]) # adds frame to the queue
				
			else:
				time.sleep(0.2) #rest for 10ms, we have a full queue
		
	def read(self):
		# returns next frame to load in the queue
		return self.Q.get()
		
	def running(self):
		return self.more() or not self.stopped
		
	def more(self):
		#returns True if there are still frames to be loaded
		while self.Q.qsize() == 0 and not self.stopped and self.tries < 5:
			time.sleep(0.1)
			self.tries += 1

		self.tries=0
	
		return self.Q.qsize() > 0 
		
	def stop(self):
		# inidcate that the thread should be stopped
		self.stopped = True
		# wait until stream resource are released
		#self.thread.join()
	

"""
class multithreadimageload:
	def __init__(self, img, transforms=None, queue_size=25):
		# initialize the process
		self.stream = torch.tensor(img,dtype=torch.float16,device=torch.device('cuda:0')).permute(2,0,1)/255
		
		self.stopped = False
		self.transfrom = transforms
		
		# Initialize the Queue
		self.Q = Queue(maxsize=queue_size)
		# initialize thread
		self.thread = Thread(target=self.update, args=())
		self.thread.daemon = True

		
	def start(self):
		# start a thread to load tensors onto gpu from frames
		self.thread.start()
		return self
		
	def update(self):
		#keep looping infinitely
		while True:
			if self.stopped:
				break
			
			if not self.Q.full():
				#Load the next image from
				frame = self.stream
				self.Q.put(frame) # adds frame to the queue
				
			else:
				time.sleep(0.1) #rest for 10ms, we have a full queue
		
	def read(self):
		# returns next frame to load in the queue
		return self.Q.get()
		
	def running(self):
		return self.more() or not self.stopped
		
	def more(self):
		#returns True if there are still frames to be loaded
		while self.Q.qsize() == 0 and not self.stopped and tries < 5:
			time.sleep(0.1)
			tries += 1
			
		return self.Q.qsize() > 0 
		
	def stop(self):
		# inidcate that the thread should be stopped
		self.stopped = True
		# wait until stream resource are released
		#self.thread.join()
"""


				
	
		
		
