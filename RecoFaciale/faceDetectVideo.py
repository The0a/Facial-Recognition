import cv2

class FaceDetectVideo:

    def __init__(self):

        # IA already trained by OpenCV (fill with path of haarcascade_frontalface_default.xml )
        face_cascade = cv2.CascadeClassifier('C:/Users/ara/PycharmProjects/Facial-Recognition/RecoFaciale/Cascades/haarcascades/haarcascade_frontalface_default.xml')

        # Video capture (webcam)
        vid = cv2.VideoCapture(0)
        
        while True:
            _, img = vid.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Face finding
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            
            # Rectangle around face 
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the output
            cv2.imshow('img', img)

            key = cv2.waitKey(30) & 0xff
            if key == 27:
                break
        vid.release()




