import cv2
import sys
import math
import numpy as np


grey_levels = 256
orig = cv2.imread('vliegtuig1.jpg',0)
orig = cv2.resize(orig, (0,0), fx=0.7, fy=0.7)
uni = cv2.copyMakeBorder(orig,0,0,0,0,cv2.BORDER_REPLICATE)

# Define the window size (16x16px)
windowsize_r = 16
windowsize_c = 16

# Crop out the window and calculate the histogram
for r in range(0,uni.shape[0] - windowsize_r, windowsize_r):
    for c in range(0,uni.shape[1] - windowsize_c, windowsize_c):
        window = uni[r:r+windowsize_r,c:c+windowsize_c]
        hist = np.histogram(window,bins=grey_levels)
