import cv2
import face_recognition
from simple_facerec import SimpleFacerec


class reco_image:

    def __init__(self):
        # Load and encode the image we want to test
        img_test = cv2.imread('test.png')
        rgb_img = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)
        encoding_img = face_recognition.face_encodings(rgb_img)[0]

        # Load and encode the image in the resources
        img_resource = cv2.imread('Images/Messi.jpeg')
        rgb_img_resource = cv2.cvtColor(img_resource, cv2.COLOR_BGR2RGB)
        encoding_img_ressource = face_recognition.face_encodings(rgb_img_resource)[0]

        result = face_recognition.compare_faces([encoding_img], encoding_img_ressource)
        print(result)


class reco_video:

    def __init__(self):

        # Encode faces in resource folder
        facerec = SimpleFacerec()
        facerec.load_encoding_images('Images/')

        # Enable the camera stream
        capture = cv2.VideoCapture(0)

        while True:
            ret, video = capture.read()

            # Detect faces
            face_location, face_name = facerec.detect_known_faces(video)
            for face_loc, name in zip(face_location, face_name):
                y1, x1, y2, x2 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                cv2.putText(video, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200), 2)
                cv2.rectangle(video, (x1, y1), (x2, y2), (0, 0, 200), 2)
            cv2.imshow("video", video)
            key = cv2.waitKey(1)
            if key == 27:
                break

        capture.release()
        cv2.destroyAllWindows()


class unlock:
    def __init__(self, name):
        if name == 'Unknown':
            print('Unknown user, access denied')
        else:
            print('Welcome ', name)
