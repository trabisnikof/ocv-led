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
	ret, frame1 = cap.read()
	prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
	hsv = np.zeros_like(frame1)
	hsv[...,1] = 255

	while(1):
   		ret, frame2 = cap.read()
    		next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    		flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

   		mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
   		hsv[...,0] = ang*180/np.pi/2
   		hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    		rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

  		self.out_pixels(rgb)
  		k = cv2.waitKey(30) & 0xff
  		if k == 27:
  		    break
  		elif k == ord('s'):
   		    cv2.imwrite('opticalfb.png',frame2)
   		    cv2.imwrite('opticalhsv.png',rgb)
   		prvs = next

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

    def out_pixels(self,image):
	img2 = Image.fromarray(cv2.resize(image,(32,32)))
	self.matrix.SetImage(img2.convert('RGB'))
# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
