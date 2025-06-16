import cv2
import math
import numpy as np


img = cv2.imread('person.bmp')


nr, nc = img.shape[:2]

x0, y0 = nr // 2, nc // 2   #定位影像中心
radius = min(x0, y0)

strength = 200   #光照強度


dst = np.zeros((nr, nc, 3), dtype="uint8")


for i in range(nr):
    for j in range(nc):
        distance = math.pow((y0-j), 2) + math.pow((x0-i), 2)   #計算現在點到光照中心的距離
        B =  img[i,j][0]
        G =  img[i,j][1]
        R = img[i,j][2]
        if (distance < radius * radius):
            result = (int)(strength*( 1.0 - math.sqrt(distance) / radius ))   #按照距離大小計算增强的光照值
            B = img[i,j][0] + result
            G = img[i,j][1] + result
            R = img[i,j][2] + result
            
            B = min(255, max(0, B))   #判斷邊界 防止越界
            G = min(255, max(0, G))   #判斷邊界 防止越界
            R = min(255, max(0, R))   #判斷邊界 防止越界
            dst[i,j] = np.uint8((B, G, R))
        else:
            dst[i,j] = np.uint8((B, G, R))

cv2.imshow('src', img)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
