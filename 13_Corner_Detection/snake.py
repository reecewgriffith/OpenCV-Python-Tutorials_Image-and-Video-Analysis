import cv2
import numpy as np

img1 = cv2.imread('board.jpg')
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img1, (x,y), 5, 255, -1)

cv2.imwrite('out.jpg', img1)