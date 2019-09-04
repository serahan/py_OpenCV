# 9/4 이미지 출력

import cv2
import numpy
import pytesseract
import matplotlib

img = cv2.imread('image.jfif', cv2.IMREAD_COLOR)
# img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_AREA)
cv2.imshow('display image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()