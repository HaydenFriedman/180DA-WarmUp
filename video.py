import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    color_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([83,100,100])
    upper_blue = np.array([103,255,255])
    mask = cv2.inRange(color_hsv,lower_blue,upper_blue)
    # Display the resulting frame
    contours,hierarchy = cv2.findContours(mask, 1, 2)
    # max_area = 0
    # max_index = 0
    # dumbX = 0
    # dumbY = 0
    # dumbW = 0
    # dumbH = 0
    # for contour in contours:
    #     area=cv2.contourArea(contour)
    #     if area>=max_area:
    #         if area>=max_area:
    #          dumbX,dumbY,dumbW,dumbH=cv2.boundingRect(contour)
    #          max_area=area

    # x,y,h,w = dumbX,dumbY,dumbW,dumbH
    # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)     
    # max_area = 0
    # max_contour = 0
    # for i in range(len(contours)):
    #     x,y,w,h = cv2.boundingRect(contours[i])
    #     if w*h > max_area:
    #         max_area = w*h
    #         max_contour = i
        
    # x,y,w,h = cv2.boundingRect(contours[max_contour])
    #cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)  
    max_area=0
    x=0
    y=0
    w=0
    h=0 
    for contour in contours:
        area=cv2.contourArea(contour)
        if area>=max_area:
            #cv2.drawContours(frame,[contour],0,(255,0,0),3)
            x,y,w,h=cv2.boundingRect(contour)
            max_area=area
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)        
    cv2.imshow("frame",frame)        
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
