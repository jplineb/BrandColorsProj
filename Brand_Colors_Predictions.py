import torch
import torchvision.transforms as transforms
from colorstuff.colorstuff import ColorResNet
import scipy
from PIL import Image
import numpy as np
import cv2
from line_profiler import LineProfiler
import time


model= torch.load('../Models/ColorResNet_0.pt')


pil2tensor = transforms.ToTensor()
tensor2pil = transforms.ToPILImage()

def normalize(img):
    norm_img=img.clone().detach()
    norm_img[0]=(norm_img[0]-.485)/.229
    norm_img[1]=(norm_img[1]-.456)/.224
    norm_img[2]=(norm_img[2]-.406)/.225
  
    return norm_img

def predict_one(img):
    #option 1
    #rgb_image = pil2tensor(img).cuda().half()#torch.tensor(img).half().cuda()
    
    #option 2
    rgb_image = torch.tensor(img,dtype=torch.float16,device=torch.device('cuda:0'))
    rgb_image = rgb_image.permute(2,0,1)
    rgb_image = rgb_image/255
    
#     orig_img=tensor2pil(rgb_image.detach().cpu().float()) # --> not used
#     orig_img.save('original.png') # --> not used
    normed=normalize(rgb_image)
#     normed_img=tensor2pil(normed.detach().cpu().float()) # --> not used
    #normed_img.save('normed.png')
    normed=normed[None]
    prediction_orig=model(normed)
    prediction =(rgb_image + .4*(2*prediction_orig-1)).clamp(0,1)
#     prediction[prediction<0]=0 #--> used clamp above
#     prediction[prediction>1]=1
#     output=tensor2pil(prediction[0].detach().cpu().float()) # --> moved below
#     output.save('corrected.png')
    
    return prediction

def livevideocorrection(filepath, modelname):
  cap = cv2.VideoCapture(filepath)
  amount_of_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
  frame_number = 7100
  last_time = time.monotonic()
  while frame_number <= amount_of_frames:
    print('Showing Frame ' + str(frame_number))
    if frame_number%10 == 0:
    	current_time = time.monotonic()
    	timedif = current_time - last_time
    	FPS = 10/timedif
    	print('FPS:' + str(FPS))
    	last_time = time.monotonic()
    	
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number-1)
    _,frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    prediction=(predict_one(frame).
                squeeze().
                detach().
                cpu().
                float())
    
    prediction=prediction.permute(1, 2, 0).numpy()
    prediction = cv2.cvtColor(prediction, cv2.COLOR_BGR2RGB)

    cv2.imshow('preview', prediction)
    cv2.waitKey(1)
    
#     prediction = original.cpu() +.6*(2*predictionmask-1)
#     prediction[prediction<0] = 0
#     prediction[prediction>1] = 1
#     predictionmask = transforms.ToPILImage()(prediction)
    
    #predictionmask.show()
    frame_number+=1



model= torch.load('../Models/ColorResNet_0.pt')
model.eval()

video='FB-112418-USCClemson-Clip13.mp4'
#livevideocorrection(video, model)

lp = LineProfiler()
lp.add_function(predict_one)
lp_wrapper = lp(livevideocorrection)
lp_wrapper(video, model)
lp.print_stats()




