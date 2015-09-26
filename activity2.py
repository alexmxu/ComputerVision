import cv2

import numpy

image1 = cv2.imread("TestImages/shops.jpg")

(bc1, gc1, rc1) = cv2.split(image1)
(bc2, gc2, rc2) = cv2.split(image1)
(bc3, gc3, rc3) = cv2.split(image1)


img1 = cv2.merge((bc1,gc1,rc1))
img2 = cv2.merge((gc2, rc2, bc2))
img3 = cv2.merge((rc3, bc3, gc3))

cv2.imshow("Cool1", img1)
cv2.imshow("Cool2", img2)
cv2.imshow("Cool3", img3)