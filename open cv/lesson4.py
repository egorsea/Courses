import cv2
import numpy as np

img = cv2.imread('.\\open cv\\tiger-gray.png')

new_img = np.zeros (img.shape, dtype = 'uint8')

# img = cv2.flip (img, 1)

def rotate (img_param, angle):
    height, width = img_param.shape[:2]
    point = (width//2, height//2)

    mat = cv2.getRotationMatrix2D (point, angle, 1)
    return cv2.warpAffine (img_param, mat, (width, height))

def tranform (img_param, x, y):
    mat = np.float32 ([[1, 0, x], [0, 1,y]])
    return cv2.warpAffine (img_param, mat, (img_param.shape[1], img_param.shape[0]))

# img = rotate (img, 45)

# img = tranform (img, 30, 200)

img = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur (img, (7, 7), 0)
img = cv2.Canny (img, 150, 150)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours (new_img, con, -1, (132,123, 231), 1)

cv2.imshow('tiger', new_img)


cv2.waitKey(10000)
