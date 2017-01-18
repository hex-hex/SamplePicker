from PyQt5.QtWidgets import *

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About me")
        self.setFixedSize(400, 400)
