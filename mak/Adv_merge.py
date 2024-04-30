import cv2
import numpy as np


def stackImages(scale, imgArray):
    # Determine number of rows and columns in the image array
    rows = len(imgArray)
    cols = len(imgArray[0])
    # Check if the first element of the array is a list (indicating multiple rows)
    rowsAvailable = isinstance(imgArray[0], list)

    # Retrieve dimensions of the images
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]

    # If images are arranged in rows
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                # Resize images to the same dimensions
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                None, scale, scale)
                # Convert grayscale images to BGR (if necessary)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        # Create a blank image with the same dimensions as the individual images
        imageBlank = np.zeros((height, width, 3), np.uint8)
        # Stack images horizontally for each row
        hor = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        # Stack rows vertically
        ver = np.vstack(hor)
    # If images are arranged in a single row
    else:
        for x in range(0, rows):
            # Resize images to the same dimensions
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            # Convert grayscale images to BGR (if necessary)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        # Stack images horizontally
        ver = np.hstack(imgArray)

    return ver

img=cv2.imread("data/md.png")

stackImages_1=stackImages(0.2,([img,img,img],[img,img,img]))

cv2.imshow("img",stackImages_1)




# cv2.imshow("img",img)
#
# img_hstack=np.hstack((img,img))
# img_vstack=np.vstack((img,img))
#
# cv2.imshow("img",img_hstack)
# cv2.imshow("img",img_vstack)

cv2.waitKey(0)