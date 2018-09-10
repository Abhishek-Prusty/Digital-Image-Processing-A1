import numpy as np 
import matplotlib.pyplot as plt 
import cv2

def plot(im,save_name):
	im=im.flatten()
	plt.hist(im,bins=256)
	plt.savefig(save_name)
	plt.gcf().clear()

dimensions=(600,400)

im=cv2.imread('A1_resources/high1.jpg',0)
im=cv2.resize(im,(dimensions))
plot(im,'high1.png')

im=cv2.imread('A1_resources/high2.jpg',0)
im=cv2.resize(im,(dimensions))
plot(im,'high2.png')

im=cv2.imread('A1_resources/high3.jpg',0)
im=cv2.resize(im,(dimensions))
plot(im,'high3.png')

im=cv2.imread('A1_resources/low1.jpg',0)
im=cv2.resize(im,(dimensions))
plot(im,'low1.png')

im=cv2.imread('A1_resources/low2.jpg',0)
im=cv2.resize(im,(dimensions))
plot(im,'low2.png')

im=cv2.imread('A1_resources/low3.jpg',0)
im=cv2.resize(im,(dimensions))
plot(im,'low3.png')