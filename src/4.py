import matplotlib.pyplot as plt
import numpy as np
import cv2

def plot_hist(im,save_name):
	im=im.flatten()
	plt.hist(im,bins=256,density=True)
	plt.savefig(save_name)
	plt.gcf().clear()


im=cv2.imread('A1_resources/lena.bmp',0)
im=cv2.resize(im,(16,16))
plot_hist(im,'lena16.png')