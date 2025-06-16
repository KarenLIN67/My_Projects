import cv2
import numpy as np

#讀取影像
img = cv2.imread('person.bmp')

#取出原始影像大小
nr, nc = img.shape[:2]

dst = np.zeros((nr, nc, 3), dtype="uint8")

for i in range(nr):
    for j in range(nc):
        B = 0.272*img[i,j][2] + 0.534*img[i,j][1] + 0.131*img[i,j][0]   #懷舊特效RBG比例
        G = 0.349*img[i,j][2] + 0.686*img[i,j][1] + 0.168*img[i,j][0]   #懷舊特效RBG比例
        R = 0.393*img[i,j][2] + 0.769*img[i,j][1] + 0.189*img[i,j][0]   #懷舊特效RBG比例
        if B>255:
            B = 255
        if G>255:
            G = 255
        if R>255:
            R = 255
        dst[i,j] = np.uint8((B, G, R))
        

cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()