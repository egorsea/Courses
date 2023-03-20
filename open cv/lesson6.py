import cv2
import numpy as np

photo = cv2.imread('.\\open cv\\tiger-color.png')


img = np.zeros (photo.shape[:2], dtype = 'uint8')

circle = cv2.circle (img.copy(), (0, 0), 80, 255, -1)   #-1 - закрасить
square = cv2.rectangle (img.copy(), (25, 25), (250, 350), 255, -1)

img = cv2.bitwise_and (photo, photo, mask=square) # пересечение
# img = cv2.bitwise_or (circle, square) # объединение
# img = cv2.bitwise_xor (circle, square) # объединение и исключение пересекаюзихя элементов
# img = cv2.bitwise_not (circle) # инверсия

cv2.imshow('Result', img)

cv2.waitKey(10000)
