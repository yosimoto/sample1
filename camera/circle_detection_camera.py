
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):

	ret, frame = cap.read()

	img = cv2.medianBlur(frame,5)
	cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

	circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,50,param1=50,param2=30,minRadius=0,maxRadius=0)
                            

	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
    		# draw the outer circle
    		cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    		# draw the center of the circle
    		cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

	cv2.imshow('frame',cimg)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
