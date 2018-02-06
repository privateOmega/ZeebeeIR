from colordescriptor import ColorDescriptor
from siftdescriptor import SiftDescriptor
from ssimdescriptor import SSIMDescriptor
import cv2
import numpy as np
import sys
from time import *
from skimage.measure import compare_ssim

def chi2_distance(histA, histB, eps = 1e-10):
    d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
        for (a, b) in zip(histA, histB)])
    return d

cd = ColorDescriptor((8, 12, 3))

imageOne = cv2.imread(sys.argv[1])
featuresOne = cd.describe(imageOne)
imageTwo = cv2.imread(sys.argv[2])
featuresTwo = cd.describe(imageTwo)
d = chi2_distance(featuresOne, featuresTwo)
print('similiarity in cd((0) - perfect match;(20) - worst)', d)

sd = SiftDescriptor()
desOne = sd.describe(imageOne)
desTwo = sd.describe(imageTwo)
print(desOne, desTwo)
bf = cv2.BFMatcher()
matches = bf.match(desOne, desTwo)
print('similiarity in sd', matches.distance)

ssim = SSIMDescriptor()
grayOne = ssim.describe(imageOne)
grayTwo = ssim.describe(imageTwo)
(score, diff) = compare_ssim(grayOne, grayTwo, full=True)
# diff = (diff * 255).astype("uint8")
# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.imshow('image', diff)
# cv2.resizeWindow('image', 600,600)
print('similiarity in ssim((1) - perfect match;(0) - worst)', score)
cv2.waitKey(0)
