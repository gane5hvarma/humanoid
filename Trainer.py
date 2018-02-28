import os
import sys
import numpy as np
import cv2
from PIL import Image

#recognizer = cv2.face.LBPHFaceRecognizer_create() this is the module not found or unable to debug, to add this to teh open-contrib/doc/face-module
#recognizer = cv2.creatLBPHFaceRecognizer()
path = 'dataset'


def getImageswithids(path):
    imagepaths = [os.path.join(path,f) for f in os.listdir(path)]
    print(imagepaths)

getImageswithids(path)
