import cv2
import numpy as np

photo = np.zeros ((450, 450, 3), dtype = 'uint8')
# BGR
photo[:] = 100 , 0, 0
photo[100:150, 200:300] = 0 , 0, 255

cv2.rectangle (photo, (0,0), (50, 50), (119, 201, 105), thickness=3)
cv2.rectangle (photo, (0,300), (50, 350), (119, 201, 105), thickness=cv2.FILLED)

cv2.line (photo, (0,photo.shape[0]//2), (100, 0), (119, 0, 105), thickness=2)
cv2.line (photo, (0,photo.shape[0]//2), (photo.shape[1], photo.shape[0]//2), (119, 0, 105), thickness=2)

cv2.circle (photo, (photo.shape[1]//2, photo.shape[0]//2),50, (119, 0, 105), thickness=cv2.FILLED)

cv2.putText (photo, 'test_image', (100, 300), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 200, 0), 2)

cv2.imshow ('Photo', photo)

cv2.waitKey(0)
