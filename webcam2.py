import cv2
import numpy
vidCap = cv2.VideoCapture(0)
x = 0
counter = 0
mod = 0
images = []
blendedimages = []
imgcounter = 0
n = 1.0
while x != 113:
    ret, img = vidCap.read()
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("test", img)
    x = cv2.waitKey(10)
    if x > -1:
        chr(x)  
    if x > -1 and x == 113:
        break
    if counter%2 == 0:
        cv2.imwrite("Pic" + str(imgcounter) + ".jpg", img)
        imgcounter +=1
        images.append(img)
    counter+=1

for i in range(len(images)/2):
    blendedimages.append(cv2.addWeighted(images[2*i+1], (0.5), images[2*i], (0.5),0))
realimg = blendedimages[0]
for j in range(len(blendedimages)-1):
    realimg = cv2.addWeighted(realimg, 1-(1.0/n), blendedimages[j+1], 1.0/n,0)
    n+=1

cv2.imshow("blendedimage", realimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

vidCap.release()