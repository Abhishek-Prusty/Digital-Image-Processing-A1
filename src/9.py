import numpy as np 
import cv2

def BinarizeImage(im,method,window_size=5):
	if(method=="otsu"):
		ret,th = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		cv2.imwrite("otsu2.jpg",th)
		cv2.imshow('Otsu binarization',th)
		cv2.waitKey(0)
		return th

	elif(method=="adaptive"):
		filt=[[1.0/(window_size*window_size) for i in range(window_size)] for j in range(window_size)]
		temp_im=cv2.filter2D(im,-1,np.array(filt))
		for i in range(len(im)):
			for j in range(len(im[i])):
				im[i][j]=255 if (im[i][j]>temp_im[i][j]) else 0
		cv2.imwrite("adaptive2.jpg",im)
		cv2.imshow('adaptive thresholding',im)
		cv2.waitKey(0)
		return im


filename="A1_resources/palm-leaf-2.jpg"
im=cv2.imread(filename,0)
cv2.imshow('Original image',im)
cv2.waitKey(0)
BinarizeImage(im,"otsu")
BinarizeImage(im,"adaptive",20)
cv2.destroyAllWindows()
