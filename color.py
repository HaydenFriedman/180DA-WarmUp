#I found that changing the color of my background was more robust than changing the lighting from my phone
#though this may have been because my phone lighting was weak
#Source code for finding dom color: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097
import numpy as np
import cv2
from sklearn.cluster import KMeans


cap = cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    color_scheme=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    target=frame[150:300,150:200,:]
    target_reshaped = target.reshape((target.shape[0]*target.shape[1],3))
    clt=KMeans(n_clusters=1, n_init="auto")
    clt.fit(target_reshaped)
    cv2.rectangle(frame, (150,150),(300,350), (0,255,0),2)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
    print(f"Dominant Color: {clt.cluster_centers_[0]}")

    # masking the image
cap.release()
cv2.destroyAllWindows()
    
