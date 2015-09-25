import cv2

leopard = cv2.imread("TestImages/SnowLeo2.jpg")


cv2.circle(leopard, (125,130), 50, (255,0,0), 1) #head
cv2.rectangle(leopard, (180, 310), (210, 400), (0, 180, 0), 0) #legs
cv2.rectangle(leopard, (320, 310), (360, 400), (0, 180, 0), 0) #legs
cv2.rectangle(leopard, (440, 310), (500, 400), (0, 180, 0), 0) #legs
cv2.rectangle(leopard, (510, 310), (560, 400), (0, 180, 0), 0) #legs

cv2.rectangle(leopard, (175, 100), (550, 300), (0, 180, 0), 0)#body

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(leopard, "SnowLeo2.jpg", (50,50), font, 2, (255,255,255)) #text

cv2.ellipse(leopard, (120, 400), (60,10), 0, 0, 180, (250, 180, 110), 0)
cv2.ellipse(leopard, (370, 425), (25,10), 0, 0, 180, (180, 250, 110), 0)
cv2.ellipse(leopard, (430, 425), (50,10), 0, 0, 180, (180, 250, 180), 0)
cv2.ellipse(leopard, (1535, 435), (30,10), 0, 0, 180, (180, 110, 250), 0) #paws

for i in range(5):
    cv2.line(leopard, (550+10*i, 120+30*i), (555+10*i, 150+30*i), (255,0,255)) #tail

cv2.imshow("Leopard", leopard)
cv2.waitKey(0)