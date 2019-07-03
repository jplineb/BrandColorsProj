from threading import Thread
import sys
import torch
import time
from queue import Queue

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

class multithreadpredict:
	def __init__(self, frame, modelname, transforms=None, queue_size=25):
		# initialize the process
		self.stream = modelname(frame)
		
		self.stopped = False
		self.transform = transforms
		
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
	
				
	
		
		
