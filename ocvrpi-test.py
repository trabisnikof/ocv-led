#!/usr/bin/env python
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

	img = cv2.imread('Black_Circle.jpg',0)
	edges = cv2.Canny(img,100,200)

	r = cv2.resize(edges,(32,32))
	img2 = Image.fromarray(r)
        canvas = self.matrix
        font = graphics.Font()
        font.LoadFont("fonts/7x13.bdf")
	self.matrix.SetImage(img2.convert('RGB'))


        time.sleep(10)   # show display for 10 seconds before exit


# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
