import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def edge_det(img):
    edges = cv2.Canny(img,100,200)

    return edges

def face_det(img):
   
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    # print(list(faces))
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return img, faces
