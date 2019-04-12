import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/zhaozijun/code/python_work/cv/face_trainer/trainer.yml')
cascadePath = '/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX

idnum = 0

names = ['zhaozijun']

cam = cv2.VideoCapture(0)
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
ok = True
while ok:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(int(minW), int(minH))
    )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        idnum, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        if confidence < 100:
            idnum = names[idnum]
            confidence = "{0}%".format(round(100 - confidence))
        else:
            idnum = "unknown"
            confidence = "{0}%".format(round(100 - confidence))
        cv2.putText(img, str(idnum), (x+5, y-5), font, 1, (0, 0, 255), 1)
        cv2.putText(img, str(confidence), (x+5, y+h-5), font, 1, (255, 255, 255), 1)
    cv2.imshow('camera', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        ok = False
cam.release()
cv2.destroyAllWindows()
