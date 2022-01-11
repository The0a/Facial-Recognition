import cv2


class FaceDetectImg:

    def __init__(self):
        count = 0
        # IA already trained by OpenCV (fill with path of haarcascade_frontalface_default.xml)
        face_cascade = cv2.CascadeClassifier('C:/Users/ara/PycharmProjects/Facial-Recognition/RecoFaciale/Cascades/haarcascades/haarcascade_frontalface_default.xml')

        # Image processing
        img=cv2.imread(r'test.png')
        gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Face finding
        faces = face_cascade.detectMultiScale(gray, 1.2, 4)


        # Rectangle around face 
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            count = count + 1

        print(count, 'faces detected')
        # Display the output
        cv2.imshow('img', img)
        cv2.waitKey()
        

     



