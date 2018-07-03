#!/usr/bin/env python
import urllib
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import cv2
import numpy as np
from PIL import Image
from PIL import ImageOps
from matplotlib import pyplot as plt

class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
	cap = cv2.VideoCapture('test.mp4')
	while(cap.isOpened()):
	    ret, frame = cap.read()
	    img2 = Image.fromarray(cv2.resize(frame,(32,32)))
            self.matrix.SetImage(img2.convert('RGB'))
            if cv2.waitKey(25) & 0xFF == ord('q'):
	       	break

	cap.release()
	cv2.destroyAllWindows()

    def url_to_image(self, url):
    	# download the image, convert it to a NumPy array, and then read
    	# it into OpenCV format
    	resp = urllib.urlopen(url)
    	image = np.asarray(bytearray(resp.read()), dtype="uint8")
    	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
    	# return the image
    	return image

# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
