import numpy as np
import cv2

def transformIntensity(im,k1,k2,a,b,name):

	retIm=np.zeros((im.shape[1],im.shape[0]))
	k1*=255
	k2*=255
	a*=255
	b*=255
	for i in range(im.shape[1]):
		for j in range(im.shape[0]):
			for k in range(len(a)):
				print(i)
				if a[k]<=im[i][j]<=b[k]:
					retIm[i][j]=im[i][k]*k1[i]+k2[i]
					break
			else:
				retIm[i][j]=im[i][j]


	#cv2.imwrite(name+'.png',retIm)
	plt.imshow(retIm)
	plt.savefig(name+'.png')
	return	retIm

im1=cv2.imread('A1_resources/lena.bmp',0)
#im1=cv2.resize(im1,(128,128))
transformIntensity(im1,[1 ,0], [0.25, 1], [0 ,0.75], [0.75, 1],"a")
transformIntensity(im1,[0, 4/3.0], [0, -1/3], [0 ,0.25], [0.25, 1],"b")
transformIntensity(im1,[0, 2, 0], [0, -0.25, 1], [0, 0.25, 0.75], [0.25, 0.75, 1],"c")
transformIntensity(im1,[0, 1, 0], [0, 0, 0], [0, 0.25, 0.75], [0.25, 0.75, 1],"d")
transformIntensity(im1,[0, 0, 0, 0], [0.25, 0.5, 0.75, 1], [0, 0.25, 0.5, 0.75], [0.25, 0.5, 0.75, 1],"e")

