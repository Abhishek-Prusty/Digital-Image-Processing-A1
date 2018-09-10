import numpy as np
import cv2
import matplotlib.pyplot as plt

def domColors(im, k, partition):
    fin = np.uint8(np.floor(im * (partition / 255)))
    elements = np.zeros(im.shape[0] * im.shape[1])
    finalarr = np.zeros(partition ** 3)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            colour = fin[i][j]
            colour[colour > partition - 1] = partition - 1
            value = colour[0] + colour[1] * partition + colour[2] * partition * partition
            finalarr[value] += 1
    vals = finalarr.argsort()[::-1][:k]
    ans = np.zeros((k, 3))
    for i in range(k):
        v = vals[i]
        if i == 0:
            print(v)
        b = v // (partition ** 2)
        g = (v - b * (partition ** 2)) // 3
        r = (v - b * (partition ** 2) - g * partition)
        b = b * (1/partition)
        g = g * (1/partition)
        r = r * (1/partition)
        ans[i] = np.array([r,g,b])
    return np.uint8(ans*255)

img=cv2.imread('A1_resources/colorful2.jpg')
k=10
print("Pallete")
out=domColors(img,k,4)
plt.figure()
for i in range(len(out)):
    plt.subplot(1,k,i+1)
    plt.axis('off')
    img=[[[out[i][2],out[i][1],out[i][0]] for x in range(50)] for j in range(50)]
    plt.imshow(np.array(img))


plt.savefig("Pallete")
plt.show()
plt.gcf().clear()



print("Dominant Colour")
img=[[[out[0][2],out[0][1],out[0][0]] for x in range(500)] for j in range(500)]
plt.axis('off')
plt.imshow(img)
plt.savefig("dominant color")
plt.show()
plt.gcf().clear()