import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelX = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobelY = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    sobel = cv2.Sobel(frame, cv2.CV_64F, 1, 1, ksize=5)
    edges = cv2.Canny(frame, 100, 100)

    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobel x', sobelX)
    cv2.imshow('sobel y', sobelY)
    cv2.imshow('sobel', sobel)
    cv2.imshow('edges', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()