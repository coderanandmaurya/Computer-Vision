import cv2
import numpy as np

img = cv2.imread("data/shape.jpg")

width,height = 720,480

pts1 = np.float32([[380,18],[706,19],[381,217],[705,218]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)