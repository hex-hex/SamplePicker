from PyQt5.QtWidgets import *
from SampleProject import *

class ProjectDialog(QDialog):
    def __init__(self, parent=None):
        super(ProjectDialog, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setFixedSize(400, 400)
        self.setWindowTitle("New Project")

