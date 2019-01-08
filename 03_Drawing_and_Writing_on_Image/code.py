import numpy as np
import cv2

img = cv2.imread('bee.jpg', cv2.IMREAD_COLOR)

#BGR for 4th parameter
#yellow
cv2.line(img, (0,0), (500,500), (0,255,255), 15)

#red
cv2.rectangle(img, (15,25), (400,300), (0,0,255), 5)

#negative line width param fills shape
#blue
cv2.circle(img, (200, 120), 50, (255,0,0), -1)

#polygons
pts = np.array([[20, 42], [88,90], [300,500], [400, 300], [10, 20]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,0), 3)

#writing text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello World', (250,250), font, 3, (255,255,255), 5, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('bee_draw.jpg', img)