import numpy as np 
import cv2
import math
import matplotlib.pyplot as plt

def chromaK(foreground,background,color,threshold):
	retIm=np.zeros((background.shape[0],background.shape[1],background.shape[2]))
	for i in range(len(background)):
		for j in range(len(background[i])):
			try:
				if abs(foreground[i][j][0]-color[0])<threshold and abs(foreground[i][j][1]-color[1])<threshold and abs(foreground[i][j][2]-color[2])<threshold:
					retIm[i][j]=background[i][j]
				else:
					retIm[i][j]=foreground[i][j]
			except:
				retIm[i][j]=background[i][j]
			finally:
				print(i," ",j)

	cv2.imwrite('chromaKeying1.png',np.asarray(retIm))
	return retIm


back=cv2.imread('A1_resources/back.png')
fore=cv2.imread('A1_resources/fore.png')
col=(0,255,0)

output=chromaK(fore,back,col,10)

result=cv2.imread('chromaKeying1.png')
cv2.imshow("output",result)
cv2.waitKey(0)
cv2.destroyAllWindows()
