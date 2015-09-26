import cv2
import numpy
vidCap = cv2.VideoCapture(0)
x = 0
counter = 0
while x != 113:
    ret, img = vidCap.read()
    #shape = numpy.ones((18,18), numpy.uint8)
    #blurimg = cv2.blur(img, (20,20), 0)
    #st = cv2.getStructuringElement(cv2.MORPH_CROSS, (30,30))
    #res = cv2.morphologyEx(img, cv2.MORPH_DILATE, st, iterations=1)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #res, img3 = cv2.threshold(img2, 89, 230, cv2.THRESH_BINARY)
    #img3 = cv2.Canny(img2, 40, 100)
    #lines = cv2.HoughLinesP(img3, 1, numpy.pi/180, threshold = 5, minLineLength = 10, maxLineGap = 10)
    #circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)    
  #  circles = np.uint16(np.around(circles))
    #for lineSet in lines:
     #   for line in lineSet:
       #     cv2.line(img, (line[0], line[1]), (line[2], line[3]), (255, 255, 0))    
    #cv2.imshow("Webcam", img3)
    #for i in circles:
      #  cv2.circle(img2, (i[0],i[1]), i[2], (0,255,0), 2)
   # cv2.imshow("circle", img2)
    #cv2.imshow("hough webcam", img)
    cv2.imshow("test", img)
    x = cv2.waitKey(10)
    if x > -  1:
        chr(x)  
    if x > -1 and x == 113:
        break
    if x > -1 and x == 32:
        cv2.imwrite("Pic" + str(counter) + ".jpg", img)
    counter+=1
cv2.destroyAllWindows()

vidCap.release()