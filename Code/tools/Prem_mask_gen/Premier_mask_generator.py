# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:19:53 2019

@author: John Paul
"""

## For this script to operate Correctlty Place the file_Correct.jpg and file_Uncorrect.jpg
## in a subdirectory labled './Data/'

## The output of this script will be filename_Difference.jpg

import cv2
import numpy as np
import os

listofimgs = os.listdir('./Data/')
wanted_photos = []

for x in listofimgs:
    photoname = x.split('_', 1)
    wanted_photos.append(photoname[0])
    
wanted_photos = list(set(wanted_photos))

for x in wanted_photos:
    alphaname = './Data/'+ x + '_Correct.jpg'
    betaname = './Data/'+ x + '_Uncorrect.jpg'
    alpha = cv2.imread(alphaname)
    
    beta = cv2.imread(betaname)
    
    diff = alpha/255 - beta/255
    diff = (diff+1)/2
    cv2.imshow('preview',diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows
    cv2.imwrite(('./Data/'+ x + '_Difference.png'), diff*255)