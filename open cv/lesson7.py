import cv2
import numpy as np

img = cv2.imread('.\\open cv\\people1.jpg')

cap = cv2.VideoCapture (0)
cap.set (3, 640)
cap.set (4, 480)
while True:
    success, img = cap.read()
    grey = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier ('.\\open cv\\faces.xml')

    results = faces.detectMultiScale (grey, scaleFactor=1.5, minNeighbors = 3)

    for (x, y, w, h) in results:
        cv2.rectangle (img, (x, y), (x+w, y+h), (0, 0 , 255), thickness=3)

    cv2.imshow('Result', img)

    if cv2.waitKey (1) & 0xFF == ord ('q'):
        break
