import cv2
import numpy as np

img = cv2.imread('.\\open cv\\tiger-gray.png')

# img = cv2.cvtColor (img, cv2.COLOR_BGR2HSV)

img = cv2.cvtColor (img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor (img, cv2.COLOR_LAB2BGR)

img = cv2.cvtColor (img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split (img)

img = cv2.merge ([b,g,r])

cv2.imshow('tiger', img)


cv2.waitKey(10000)
