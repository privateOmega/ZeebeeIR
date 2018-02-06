import numpy as np
import cv2

class SSIMDescriptor:
    def __init__(self):
        pass
    
    def describe(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return image
