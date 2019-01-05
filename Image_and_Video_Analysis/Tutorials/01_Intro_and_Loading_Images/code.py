import cv2
import numpy as np
import matplotlib.pyplot as plt

#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0
img = cv2.imread('bee.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,300],[200,300], 'c', linewidth=5)
#plt.show()

cv2.imwrite('bee_gray.jpg', img)
