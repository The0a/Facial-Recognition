import sys

import Recognition, faceDetectImg, faceDetectVideo
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Frame")

        self.btn_unlock = QPushButton()
        self.btn_unlock.setText('Unlock with face recognition')
        self.btn_unlock.clicked.connect(lambda: Recognition.reco_video())

        self.btn_img_detect = QPushButton()
        self.btn_img_detect.setText('Test face detection on picture')
        self.btn_img_detect.clicked.connect(lambda: faceDetectImg.FaceDetectImg())

        self.btn_video_detect = QPushButton()
        self.btn_video_detect.setText('Test face detection on video')
        self.btn_video_detect.clicked.connect(lambda: faceDetectVideo.FaceDetectVideo())

        layout = QGridLayout(self)

        layout.addWidget(self.btn_img_detect)
        layout.addWidget(self.btn_video_detect)
        layout.addWidget(self.btn_unlock)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
