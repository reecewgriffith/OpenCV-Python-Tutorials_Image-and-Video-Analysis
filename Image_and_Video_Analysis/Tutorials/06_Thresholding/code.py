import cv2
import numpy as np

#BOOK PAGE
img1 = cv2.imread('page.jpg')

retval1, threshold1 = cv2.threshold(img1, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval3, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img1)
cv2.imshow('binary', threshold1)
cv2.imshow('gray binary', threshold2)
cv2.imshow('adaptive gaus', gaus)
cv2.imshow('otsu', otsu)

#SPIDER
img2_i = cv2.imread('spider.jpg')
img2 = cv2.resize(img2_i, (0,0), fx=0.5, fy=0.5)

retval4, threshold4 = cv2.threshold(img2, 12, 255, cv2.THRESH_BINARY)

grayscaled2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
retval5, threshold5 = cv2.threshold(grayscaled2, 12, 255, cv2.THRESH_BINARY)

gaus2 = cv2.adaptiveThreshold(grayscaled2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval6, otsu2 = cv2.threshold(grayscaled2, 125, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('original', img2)
cv2.imshow('binary', threshold4)
cv2.imshow('gray binary', threshold5)
cv2.imshow('adaptive gaus', gaus2)
cv2.imshow('otsu', otsu2)

cv2.waitKey(0)
cv2.destroyAllWindows()