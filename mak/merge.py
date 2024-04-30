import cv2
import numpy as np

img=cv2.imread("data/md.png")

cv2.imshow("img",img)

img_hstack=np.hstack((img,img))
img_vstack=np.vstack((img,img))

cv2.imshow("img",img_hstack)
cv2.imshow("img",img_vstack)

cv2.waitKey(0)