import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#changing capture resolution
cap.set(3, 400)
cap.set(4, 400)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #standard blurring
    kernel = np.ones((7,7), np.float32)/(7*7)
    smoothed = cv2.filter2D(res, -1, kernel)

    #gaussian
    blur = cv2.GaussianBlur(res, (7,7), 0)
    median = cv2.medianBlur(res, 7)

    #bilateral
    bilateral = cv2.bilateralFilter(res, 7, 75, 75)


    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('blurred', smoothed)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

#camera release
cap.release()