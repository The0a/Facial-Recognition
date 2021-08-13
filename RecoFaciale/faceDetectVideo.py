import cv2

class FaceDetectVideo:

    def __init__(self):
        #Modeles d'IA pre-entraines, distribue par OpenCV
        face_cascade = cv2.CascadeClassifier('D:\Projets visual studio\RecoFaciale\RecoFaciale\Cascades\haarcascades\haarcascade_frontalface_default.xml')

        #Capture de video (webcam)
        vid = cv2.VideoCapture(0)
        
        while True:
            _, img = vid.read()
            gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #Detection de visage
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            #TODO : si visage detecte -> afficher un message avec le nombre de visage
            

            #Mise en valeur du visage 
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Display the output
            cv2.imshow('img', img)

            key = cv2.waitKey(30) & 0xff
            if key == 27:
                break
        vid.release()




