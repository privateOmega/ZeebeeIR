import numpy as np
import cv2

class SiftDescriptor:
    def __init__(self):
        pass
    
    def describe(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()
        (kp, des) = sift.detectAndCompute(gray, None)
        return des
