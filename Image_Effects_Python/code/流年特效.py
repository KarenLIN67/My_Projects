import cv2
import math
import numpy as np


img = cv2.imread('person.bmp')


nr, nc = img.shape[:2]


dst = np.zeros((nr, nc, 3), dtype="uint8")


for i in range(nr):
    for j in range(nc):
        B = math.sqrt(img[i,j][0]) * 12   #開根號 * 參數(12最剛好)
        G =  img[i,j][1]
        R =  img[i,j][2]
        if B>255:
            B = 255
        dst[i,j] = np.uint8((B, G, R))
        
        
cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()