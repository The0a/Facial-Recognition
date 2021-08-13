import cv2

class FaceDetectImg:

    def __init__(self):
        #Modeles d'IA pre-entraines, distribue par OpenCV
        face_cascade = cv2.CascadeClassifier('D:\Projets visual studio\RecoFaciale\RecoFaciale\Cascades\haarcascades\haarcascade_frontalface_default.xml')

        #Traitement de l'image
        img=cv2.imread(r'image.jpg')
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Detection de visage
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        #Mise en valeur du visage 
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Display the output
        cv2.imshow('img', img)
        cv2.waitKey()
        

     



