import cv2
import numpy as np

# img = cv2.imread('.\\open cv\\tiger-gray.png')
#
# cv2.imshow('tiger', img)
#
# cv2.waitKey(1000)

cap = cv2.VideoCapture (0)
cap.set (3, 640)
cap.set (4, 480)

while True:
    success, img = cap.read()

    # img = cv2.resize (img, (img.shape[1], img.shape[0]//2))


    img = cv2.GaussianBlur (img, (7, 7), 0)
    img = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny (img, 30, 30)

    kernel = np.ones ((5, 5), np.uint8)
    # img = cv2.dilate (img, kernel, iterations =1)

    # img = cv2.erode (img, kernel, iterations =1)

    cv2.imshow ('Result', img)

    if cv2.waitKey (1) & 0xFF == ord ('q'):
        break
