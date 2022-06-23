#dataSet.py
import cv2
import os
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)#set video height
face_detector = cv2.CascadeClassifier('C:\\Users\\DELL\\Desktop\\haarcascade_frontalface_default.xml')
print("\n initializing face capture ....Look at the camera and wait")
count=0
while(True):
    img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)
    name = 1
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h),(0,255,0),thickness=4)
        count +=1
        cv2.imwrite("dataset."+str(name)+'.'+str(count)+".jpg",gray[y:y+h, x:x+w]);
        cv2.imshow('image',img)
        k= cv2.waitKey(2000)
        if k==27:
            break
        elif count>=30:
            break
print("\n Exciting  program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
