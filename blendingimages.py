import cv2

import numpy

image = cv2.imread("Pic75.jpg")
image2 = cv2.imread("Pic104.jpg")
image3 = cv2.imread("Pic126.jpg")
image4 = cv2.imread("Pic146.jpg")
image5 = cv2.imread("Pic190.jpg")
image6 = cv2.imread("Pic171.jpg")
image7 = cv2.imread("Pic190.jpg")
image8 = cv2.imread("Pic234.jpg")
image9 = cv2.imread("Pic318.jpg")
image10 = cv2.imread("Pic337.jpg")
image11 = cv2.imread("Pic372.jpg")
image12 = cv2.imread("Pic421.jpg")



#cv2.imshow("coin1", image)
#cv2.imshow("coin2", image2)

image1new = cv2.resize(image, (680,453))
image2new = cv2.resize(image2, (680,453))
image3new = cv2.resize(image3, (680,453))
image4new = cv2.resize(image4, (680,453))
image5new = cv2.resize(image5, (680,453))
image6new = cv2.resize(image6, (680,453))
image7new = cv2.resize(image7, (680,453))
image8new = cv2.resize(image8, (680,453))
image9new = cv2.resize(image9, (680,453))
image10new = cv2.resize(image10, (680,453))
image11new = cv2.resize(image11, (680,453))
image12new = cv2.resize(image12, (680,453))



#cv2.imshow("image2new", image2new)

blendedimage1 = cv2.addWeighted(image1new, 0.2, image2new, 0.8,0)
blendedimage2 = cv2.addWeighted(image3new, 0.2, image8new, 0.8,0)
blendedimage3 = cv2.addWeighted(image4new, 0.2, image9new, 0.8,0)
blendedimage4 = cv2.addWeighted(image5new, 0.2, image10new, 0.8,0)
blendedimage5 = cv2.addWeighted(image6new, 0.2, image11new, 0.8,0)
blendedimage6 = cv2.addWeighted(image7new, 0.2, image12new, 0.8,0)

blendedimage1a = cv2.addWeighted(blendedimage1, 0.5, blendedimage2, 0.5,0)
blendedimage2a = cv2.addWeighted(blendedimage3, 0.5, blendedimage4, 0.5,0)
blendedimage3a = cv2.addWeighted(blendedimage5, 0.5, blendedimage6, 0.5,0)

blendedimage1b = cv2.addWeighted(blendedimage1a, 0.5, blendedimage2a, 0.5,0)

blendedimage1c = cv2.addWeighted(blendedimage1b, 0.67, blendedimage3a, 0.33,0)

cv2.imshow("blendedimage", blendedimage1c)
