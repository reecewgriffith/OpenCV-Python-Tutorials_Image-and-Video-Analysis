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

    #converting to HSV,
    # but won't work for this range operation
    #dark_red = np.uint8([[12,22,121]])
    #dark_red = cv2.cvtColor((dark_red, cv2.COLOR_BGR2HSV))

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

#camera release
cap.release()