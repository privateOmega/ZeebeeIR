from colordescriptor import ColorDescriptor
from siftdescriptor import SiftDescriptor
import cv2
import numpy as np
import sys
from time import *

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
print('similiarity in cd', d)

sd = SiftDescriptor()
desOne = sd.describe(imageOne)
desTwo = sd.describe(imageTwo)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(desOne, desTwo)
print('similiarity in sd', matches.distance)

