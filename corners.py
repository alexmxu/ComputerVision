import cv2

img1 = cv2.imread("TestImages/Puzzle1.jpg")

grayImg = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

goodFeats = cv2.goodFeaturesToTrack(grayImg, 100, 0.1, 5)

for i in goodFeats:
    print i
    cv2.circle(grayImg, (i[0][0],i[0][1]), 50, (255,0,0), 1)
    
cv2.imshow("img", grayImg)