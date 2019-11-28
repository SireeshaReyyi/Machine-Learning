import cv2 

face_cascade =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
cap = cv2.VideoCapture(0)
 

while True: 
    ret, img = cap.read() 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
			
 
    for (x,y,w,h) in faces:
       
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        cv2.imwrite('sample.jpg',img)
        
        
    cv2.imshow('img',img)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()