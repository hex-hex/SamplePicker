from PyQt5.QtWidgets import *

class ProjectDialog(QDialog):
    def __init__(self, parent=None):
        super(ProjectDialog, self).__init__(parent)
        self.m_projectInfo = {}
        self.initUI()

    def initUI(self):
        self.m_confirm = False

        self.setFixedSize(450, 270)
        self.m_formerPath = QTextEdit(self)
        self.m_formerPath.resize(350, 25)
        self.m_formerPath.move(20, 30)
        self.m_formerButton = QPushButton('Open', self)
        self.m_formerButton.clicked.connect(self.onButtonFormer)
        self.m_formerButton.resize(55, 25)
        self.m_formerButton.move(380, 30)

        self.m_newerPath = QTextEdit(self)
        self.m_newerPath.resize(350, 25)
        self.m_newerPath.move(20, 100)
        self.m_newerButton = QPushButton('Open', self)
        self.m_newerButton.clicked.connect(self.onButtonNewer)
        self.m_newerButton.resize(55, 25)
        self.m_newerButton.move(380, 100)

        self.m_projectPath = QTextEdit(self)
        self.m_projectPath.resize(350, 25)
        self.m_projectPath.move(20, 170)
        self.m_projectButton = QPushButton('Save', self)
        self.m_projectButton.clicked.connect(self.onButtonProject)
        self.m_projectButton.resize(55, 25)
        self.m_projectButton.move(380, 170)

        self.m_okButton = QPushButton('OK', self)
        self.m_okButton.resize(80, 25)
        self.m_okButton.move(240, 220)
        self.m_okButton.clicked.connect(self.onButtonOK)
        self.m_cancelButton = QPushButton('Cancel', self)
        self.m_cancelButton.resize(80, 25)
        self.m_cancelButton.move(340, 220)
        self.m_cancelButton.clicked.connect(self.onButtonCancel)

        self.setWindowTitle("New Project")

    def onButtonFormer(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open a exist project file", "",
                                                  "JPEG Image Files (*.jpg);;TIFF Image Files (*.tif);;All Files (*)")
        self.m_formerPath.setText(fileName)

    def onButtonNewer(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open a exist project file", "",
                                                  "JPEG Image Files (*.jpg);;TIFF Image Files (*.tif);;All Files (*)")
        self.m_newerPath.setText(fileName)

    def onButtonProject(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Open a exist project file", "",
                                                  "DataBase Files (*.db);;All Files (*)")
        fileName = fileName[0:-3] + r'.cdsp.db'
        self.m_projectPath.setText(fileName)

    def onButtonOK(self):
        self.m_projectInfo['FORMER_IMG'] = self.m_formerPath.toPlainText()
        self.m_projectInfo['NEWER_IMG'] = self.m_newerPath.toPlainText()
        self.m_projectInfo['PROJECT_FILE'] = self.m_projectPath.toPlainText()
        self.m_confirm = True
        self.close()

    def onButtonCancel(self):
        self.close()
