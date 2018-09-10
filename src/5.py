import numpy as np 
import matplotlib.pyplot as plt 
import cv2
import math


def normHistogramIm(im):
	count=[0.0 for i in range(256)]
	for i in range(len(im)):
		for j in range(len(im[i])):
			count[im[i][j]]+=1.0
	count=[count[i]*(1.0/(im.shape[0]*im.shape[1])) for i in range(256)]
	return count

def cdf(pdf):
	cdfIm=[0 for i in range(256)]
	cdfIm[0]=pdf[0]
	for i in range(1,256):
		cdfIm[i]=pdf[i]+cdfIm[i-1]
	return cdfIm

def histEqualization(im,name):
	histIm=normHistogramIm(im)
	equalizedIm=[[0 for i in range(im.shape[1])] for j in range(im.shape[0])]
	mapping={}
	for i in range(0,256):
		value=0
		for j in range(i):
			value+=histIm[j]
		mapping[i]=math.floor(255*value)

	for i in range(im.shape[0]):
		for j in range(im.shape[1]):
			print(i," ",j)
			equalizedIm[i][j]=mapping[im[i][j]]

	cv2.imwrite(name,np.array(equalizedIm))

def histMatching(im1,im2,name):
	mapping_dict={}
	pdf1=normHistogramIm(im1)
	cdf1=cdf(pdf1)
	pdf2=normHistogramIm(im2)
	cdf2=cdf(pdf2)
	for i in range(256):
		min_diff=999999
		for j in range(256):
			if abs(cdf2[j]-cdf1[i])<min_diff:
				min_diff=abs(cdf2[j]-cdf1[i])
				approx=j
		mapping_dict[i]=approx

	for i in range(im1.shape[0]):
		for j in range(im1.shape[1]):
			print(i," ",j)
			im1[i][j]=mapping_dict[im1[i][j]]

	cv2.imwrite(name,im1)


def localHistEqualization(im,name,window_size):
	retIm=np.zeros(im.shape)
	retIm=cv2.copyMakeBorder(im,window_size//2,window_size//2,window_size//2,window_size//2,cv2.BORDER_REPLICATE)
	for i in range(window_size//2,len(retIm)-window_size//2):
		for j in range(window_size//2,len(retIm[i])-window_size//2):
			print(i," ",j)
			neighbourhood=retIm[i-window_size//2:i+window_size//2,j-window_size//2:j+window_size//2]
			pdf1=normHistogramIm(neighbourhood)
			count=cdf(pdf1)
			retIm[i-window_size//2][j-window_size//2]=math.floor(255*count[retIm[i][j]])
	cv2.imwrite(name,retIm)


im=cv2.imread('A1_resources/hist_equal2.jpg',0)
#im=cv2.resize(im,(256,256))
#histEqualization(im,"equalized2.jpg")
localHistEqualization(im,"local_equalized2_5.jpg",5)

im1=cv2.imread('A1_resources/hist-match-1.jpg',0)
im2=cv2.imread('A1_resources/hist-match-2.jpg',0)
#histMatching(im1,im2,"matched.jpg")
