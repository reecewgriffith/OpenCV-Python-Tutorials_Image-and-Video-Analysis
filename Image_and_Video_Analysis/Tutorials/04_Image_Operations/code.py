import cv2
import numpy as np

img = cv2.imread('bee.jpg', cv2.IMREAD_COLOR)
dimensions = img.shape
height = dimensions[0]
width = dimensions[1]
channels = dimensions[2]

print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)

px = img[200,200]
px = [255,255,255]
print(px)

#ROI - region of image
roi = img[30:50,100:150]
roi = [255,255,255]
print(roi)

#could just directle assign this to [255,255,255]
img[100:150,100:150] = roi

bee_zoom = img[150:400, 100:475]
img[0:(height-250),(width-375 ):width] = bee_zoom

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()