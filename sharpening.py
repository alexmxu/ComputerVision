import cv2
import numpy

image = cv2.imread("TestImages/SnowLeo2.jpg")
cv2.imshow("original", image)
blurimage = cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("blurred", blurimage)
blendedimage = cv2.addWeighted(image, 1.5, blurimage, -0.5,0)
cv2.imshow("blended", blendedimage)
cv2.waitKey(0)
cv2.destroyAllWindows()