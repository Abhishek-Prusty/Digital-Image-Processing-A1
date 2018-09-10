import numpy as np
import cv2

def bit_planes(im):
	for bit in range(0,8):
		mask=128
		mask=mask>>bit
		ret=np.bitwise_and(im,mask)
		ret=(ret/mask)*255
		filename='bit-plane-'+str(bit+1)
		cv2.imwrite(filename+'.png',ret)
		cv2.imshow(filename,ret)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

im=cv2.imread('A1_resources/lena.bmp',0)
bit_planes(im)