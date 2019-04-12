import cv2
import os
import datetime

cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
face_id = input('\n enter user id:')
print('\n Initializing face capture. Look at the camera and wait ...')
count = 0
ok = True
ISOTIMEFORMAT='%Y-%m-%d@%H:%M:%S'
while ok:
    sucess, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+w), (255, 0, 0))
        count += 1
        theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        cv2.imwrite("Facedata/User_" + str(face_id) + '_' + theTime + '#' +str(count) + '.jpg', gray[y: y + h, x: x + w])
        cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        ok = False
    elif count >= 500:
        ok = False

cap.release()
cv2.destroyAllWindows()
