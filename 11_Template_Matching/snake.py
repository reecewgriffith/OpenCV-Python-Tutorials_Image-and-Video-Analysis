import cv2
import numpy as np

###############################################################################

#functions
def template_match(img_rgb, img_gray, template, thresh):

    t_w, t_h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= thresh)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + t_w, pt[1] + t_h), (0, 255, 255), 2)

###############################################################################

#main
img_rgb = cv2.imread('chess.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
img_gray_inv = cv2.bitwise_not(img_gray)

thresh = 0.9

template = cv2.imread('white_DSP.jpg', 0)
template_match(img_rgb, img_gray, template, thresh)

template = cv2.imread('white_LSP.jpg', 0)
template_match(img_rgb, img_gray, template, thresh)

template = cv2.imread('black_DSP.jpg', 0)
template_match(img_rgb, img_gray, template, thresh)

template = cv2.imread('black_LSP.jpg', 0)
template_match(img_rgb, img_gray, template, thresh)

cv2.imwrite('chess_res.jpg', img_rgb)