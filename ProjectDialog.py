from PyQt5.QtWidgets import *

class ProjectDialog(QDialog):
    def __init__(self, parent=None):
        super(ProjectDialog, self).__init__(parent)
        self._projectInfo = {}
        self.initUI()

    def initUI(self):
        self.setFixedSize(450, 270)
        self._formerPath = QTextEdit(self)
        self._formerPath.resize(350, 25)
        self._formerPath.move(20, 30)
        self._formerButton = QPushButton('Open', self)
        self._formerButton.clicked.connect(self.onButtonFormer)
        self._formerButton.resize(55, 25)
        self._formerButton.move(380, 30)

        self._newerPath = QTextEdit(self)
        self._newerPath.resize(350, 25)
        self._newerPath.move(20, 100)
        self._newerButton = QPushButton('Open', self)
        self._newerButton.clicked.connect(self.onButtonNewer)
        self._newerButton.resize(55, 25)
        self._newerButton.move(380, 100)

        self._projectPath = QTextEdit(self)
        self._projectPath.resize(350, 25)
        self._projectPath.move(20, 170)
        self._projectButton = QPushButton('Save', self)
        self._projectButton.clicked.connect(self.onButtonProject)
        self._projectButton.resize(55, 25)
        self._projectButton.move(380, 170)

        self._okButton = QPushButton('OK', self)
        self._okButton.resize(80, 25)
        self._okButton.move(240, 220)
        self._okButton.clicked.connect(self.onButtonOK)
        self._cancelButton = QPushButton('Cancel', self)
        self._cancelButton.resize(80, 25)
        self._cancelButton.move(340, 220)
        self._cancelButton.clicked.connect(self.onButtonCancel)

        self.setWindowTitle("New Project")

    def onButtonFormer(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open a exist project file", "",
                                                  "JPEG Image Files (*.jpg);;TIFF Image Files (*.tif);;All Files (*)")
        self._formerPath.setText(fileName)
        print(fileName)

    def onButtonNewer(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open a exist project file", "",
                                                  "JPEG Image Files (*.jpg);;TIFF Image Files (*.tif);;All Files (*)")
        self._newerPath.setText(fileName)
        print(fileName)

    def onButtonProject(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Open a exist project file", "",
                                                  "DataBase Files (*.db);;All Files (*)")
        self._projectPath.setText(fileName)
        print(fileName)

    def onButtonOK(self):
        print("OK")
        self._projectInfo['FORMER_IMG'] = self._formerPath.toPlainText()
        self._projectInfo['NEWER_IMG'] = self._newerPath.toPlainText()
        self._projectInfo['PROJECT_FILE'] = self._projectPath.toPlainText()
        self.close()

    def onButtonCancel(self):
        print('Cancel')
        self.close()
