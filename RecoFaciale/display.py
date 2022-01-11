import sys
import Recognition
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.btn_unlock = QPushButton()
        self.btn_unlock.setText('Unlock with face recognition')
        self.btn_unlock.clicked.connect(lambda: Recognition.reco_video())

        layout = QGridLayout(self)
        layout.addWidget(self.btn_unlock)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
