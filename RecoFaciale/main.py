import faceDetectImg
import faceDetectVideo
import Recognition

class main:

    print("1. Image \n2. Webcam\n")
    answer = input()
    if answer == '1':
        faceDetectImg.FaceDetectImg()
    elif answer == '2':
        faceDetectVideo.FaceDetectVideo()
    elif answer == '3':
        Recognition.reco_video()


