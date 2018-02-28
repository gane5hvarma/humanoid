import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(1)
''' Before detecting the face, Identifier(id) detects the name of the face'''
id = input('enter the user id: ')
samplenum = 0;
while cap.isOpened():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 10, 5)

    for (x,y,w,h) in faces:
        samplenum = samplenum+1
        cv2.imwrite("dataset/User_"+str(id)+"_"+str(samplenum)+".jpg", gray[y:y+h,x:x+w]) #format of the image name user.id.sampleNo.
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.waitKey(1000)
    cv2.imshow('img',img)
    #cv2.waitKey(30)
    if(samplenum > 20):
        break
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()

