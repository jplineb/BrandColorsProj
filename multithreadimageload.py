from threading import Thread
import sys
import torch
import torchvision.transforms as transforms
import time
import cv2
from queue import Queue

class ColorCorrector:
	
	# class members
	norm_mu = torch.tensor([0.485, 0.456, 0.406], dtype=torch.float16,device=torch.device('cuda:0')).reshape(3,1,1)
	norm_sd = torch.tensor([0.229, 0.224, 0.225], dtype=torch.float16,device=torch.device('cuda:0')).reshape(3,1,1)
	
	def __init__(self, model, intensity=0.4):
		self.model=model
		self.intensity=intensity
	 
	def predict(self, rgb_image, frame_number):

		if frame_number%1 == 0 or frame_number <= 5:
			img_normed = ColorCorrector._normalize(rgb_image)[None]
			self.prediction_orig = self.model(img_normed)

		prediction =rgb_image + self.intensity*2.0*self.prediction_orig-self.intensity

		return prediction.clamp(0,1)
		
	@classmethod
	def _normalize(cls, img):
		norm_img=img.clone().detach()
		return (norm_img - cls.norm_mu)/cls.norm_sd

class InferenceDataStream:
	
	def __init__(self, fvs, model, transforms=None, queue_size=25):
		
		# initialize the process
		self.stream = fvs
		self.model = model
		self.stopped = False
		self.transfrom = transforms
		
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
				img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
				# format tensor type
				frame = torch.tensor(img,dtype=torch.float16,device=torch.device('cuda:0')).permute(2,0,1)/255

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


				
	
		
		
