import numpy as np 
import cv2
import matplotlib.pyplot as plt 


def BitQuantizeImage(im,k):
	if(k<8):
		factor=2**(8-k)
		ret=im//factor
		return factor*ret 
	else:
		return im
def display(im):
	plt.figure()
	for k in range(1,9):
		quantized=BitQuantizeImage(im,k)
		name=str(k)+'bit quantized image'
		cv2.imwrite(name+'.png',quantized)
		cv2.imshow(name,quantized)
		cv2.waitKey(0)
		cv2.destroyAllWindows()


im=cv2.imread('A1_resources/lena.bmp',0)
k=3
quantized_im=BitQuantizeImage(im,k)
display(im)
cv2.imwrite('quantized_image.png',quantized_im)

