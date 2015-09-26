import cv2

img1 = cv2.imread("TestImages/SnowLeo3.jpg")

img2 = cv2.imread("TestImages/SnowLeo2.jpg")

gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])

bp = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

cv2.imshow("BackProject", bp)
cv2.imshow("histogram1", hist1)
cv2.imshow("histogram2", hist2)
cv2.waitKey(0)

cv2.destroyAllWindows()