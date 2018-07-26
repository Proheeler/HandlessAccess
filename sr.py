import cv2
import numpy as np

cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
ret,frame = cap.read() # return a single frame in variable `frame`
cv2.imwrite('c4.jpg',frame)
# while(True):
    # cv2.imshow('img1',frame) #diysplay the captured image
    # if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
        # cv2.imwrite('match.jpg',frame)
        # cv2.destroyAllWindows()
        # break

# cap.release()