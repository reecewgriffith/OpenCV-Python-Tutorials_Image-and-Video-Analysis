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

    #erosion: if pixel in area is not same color, remove,
    # pushing pixels out to remove noise
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    #opening: removing false positives (noise in non-red)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    #closing: removing false negatives (noise in red)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    #Tophat: difference between opening of input image and input image
    th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)

    #Blackat: difference between closing of input image and input image
    bh = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('tophat', th)
    cv2.imshow('blackhat', bh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

#camera release
cap.release()