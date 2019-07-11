import torch
import torchvision.transforms as transforms
from colorstuff.colorstuff import ColorResNet
import numpy as np
import cv2
from line_profiler import LineProfiler
import time

from multithreadimageload import InferenceDataStreamRT

from imutils.video import FileVideoStream
import argparse
import imutils

import psutil
import numpy as np

import pycuda.driver as cuda
# This import causes pycuda to automatically manage CUDA context creation and cleanup.
import pycuda.autoinit

import tensorrt as trt

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], ".."))

# You can set the logger severity higher to suppress messages (or lower to display more messages).
TRT_LOGGER = trt.Logger(trt.Logger.WARNING)


##### Define engine functions for building before model starts #######

def allocate_buffers(engine):
    # Determine dimensions and create page-locked memory buffers (i.e. won't be swapped to disk) to hold host inputs/outputs.
    h_input = cuda.pagelocked_empty(trt.volume(engine.get_binding_shape(0)), dtype=trt.nptype(ModelData.DTYPE))
    h_output = cuda.pagelocked_empty(trt.volume(engine.get_binding_shape(1)), dtype=trt.nptype(ModelData.DTYPE))
    # Allocate device memory for inputs and outputs.
    d_input = cuda.mem_alloc(h_input.nbytes)
    d_output = cuda.mem_alloc(h_output.nbytes)
    # Create a stream in which to copy inputs/outputs and run inference.
    stream = cuda.Stream()
    return h_input, d_input, h_output, d_output, stream
    
    
def build_engine_onnx(model_file):
	with trt.Builder(TRT_LOGGER) as builder, builder.create_network() as network, trt.OnnxParser(network, TRT_LOGGER) as parser:
	    builder.max_workspace_size = 1 << 30
	    builder.max_batch_size = 5
	    builder.fp16_mode = True
	    
	    
	    # Load the Onnx model and parse it in order to populate the TensorRT network.
	    with open(model_file, 'rb') as model:
	        parser.parse(model.read())
	    return builder.build_cuda_engine(network)
	    
## Create inference function ##

def do_inference(context, h_input, d_input, h_output, d_output, stream):
    # Transfer input data to the GPU.
    cuda.memcpy_htod_async(d_input, h_input, stream)
    # Run inference.
    context.execute_async(bindings=[int(d_input), int(d_output)], stream_handle=stream.handle)
    # Transfer predictions back from the GPU.
    cuda.memcpy_dtoh_async(h_output, d_output, stream)
    # Synchronize the stream
    stream.synchronize()

	 
#######################################################################

## Define starting variabls within a class ##
class ModelData(object):
	MODEL_PATH = "./ColorResnet_onnx.onnx"
	VIDEO_PATH = './Clip_2_trim.mp4'
	DTYPE = trt.float16


## Create Video Stream ##
fvs = FileVideoStream(ModelData.VIDEO_PATH, queue_size=15).start()
ivs = InferenceDataStreamRT(fvs, queue_size=15).start()

## Create Normalization Function (to be replaced with class later) ##

def normalize_image(image):
		#norm_img = image.copy()
		#norm_img = cv2.cvtColor(norm_img, cv2.COLOR_BGR2RGB)
		#norm_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) --> moved to class
		#norm_img = norm_img.transpose([2, 0, 1])/255 --> moved to class
		#norm_img[0]=(norm_img[0]-.485)/.229 --> moved to class
		#norm_img[1]=(norm_img[1]-.456)/.224 --> moved to class
		#norm_img[2]=(norm_img[2]-.406)/.225 --> moved to class
		#print("Shape of image before ravel: ")
		#print(norm_img)
		#norm_img = norm_img.ravel() --> moved to class
		return norm_img


def load_normalized_test_case(test_image, pagelocked_buffer):
	# Normalize the image and copy to pagelocked memory.
	test_image = test_image.ravel()
	np.copyto(pagelocked_buffer, test_image)
	return test_image
	
def InferStuff(filestream, h_input, d_input, h_output, d_output, stream, context, frame_number):
	# Load a normalized test case into the host input page-locked buffer.
	test_image = filestream.read()
	test_case = load_normalized_test_case(test_image[0], h_input)
	do_inference(context, h_input, d_input, h_output, d_output, stream)
	#print(h_output) # output from inference
	# Postprocess the image for display
	outputimg = (h_output.reshape([3,720,1280])).astype('float32')
	

	outputimg = test_image[1]/255 + 1.5*(2*outputimg.transpose(1,2,0)-1)
	#print(outputimg.shape)
	#outputimg = cv2.cvtColor(outputimg, cv2.COLOR_BGR2RGB)
	# update display
	cv2.imshow('preview', outputimg)
	cv2.waitKey(1)
	frame_number+=1
	
	return frame_number

## Function for looping over video ##
def livevideocorrection():
	class ModelData(object):
		MODEL_PATH = "./ColorResnet_onnx.onnx"
		VIDEO_PATH = './clip2'
		DTYPE = trt.float16
	desired_frames = 100
	frame_number = 0
	last_time = time.monotonic()
	with build_engine_onnx('./ColorResNet_onnx.onnx') as engine:
		# Allocate buffers and create a CUDA stream.
		h_input, d_input, h_output, d_output, stream = allocate_buffers(engine)
		# Contexts are used to perform inference.
		
		with engine.create_execution_context() as context:
			while ivs.more() and frame_number <= desired_frames:
				if frame_number%5 == 0:
					current_time = time.monotonic()
					timedif = current_time - last_time
					FPS = 5/timedif
					print('FPS:' + str(FPS))
					last_time = time.monotonic()
				frame_number = InferStuff(ivs, h_input, d_input, h_output, d_output, stream, context, frame_number)
			
		# Clean up enviroment
		cv2.destroyAllWindows()
		fvs.stop()


if __name__=='__main__':
		lp = LineProfiler()
		#lp.add_function(InferStuff)
		#lp.add_function(load_normalized_test_case)
		#lp.add_function(normalize_image)
		#lp.add_function(do_inference)
		lp_wrapper = lp(livevideocorrection)
		lp_wrapper()
		lp.print_stats()
	
	
