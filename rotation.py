import cv2
import numpy

img = cv2.imread("TestImages/SnowLeo2.jpg")

def rotateImage(image):
    (rows, cols, depth) = image.shape
    rotMat = cv2.getRotationMatrix2D( (cols / 2, rows / 2), 45, 1)
    rotImg = cv2.warpAffine(image, rotMat, (cols, rows))
    cv2.imshow("Rotated", rotImg)
    return rotImg


cv2.imshow("Original", img)

while (1==1):
    x = cv2.waitKey(10)
    if x > -1 and x == 32:
        img = rotateImage(img)
        cv2.imshow("rotated", img)
    if x > -1 and chr(x) == 'q':
        break
cv2.waitKey(0)
cv2.destroyAllWindows()

