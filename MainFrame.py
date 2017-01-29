import sys
import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from SampleProject import *
from ProjectDialog import *
from AboutDialog import *

class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setWindowTitle('C D S P  by hugh')
        self._mainProject = ProjectSet()

        thisMenu = self.menuBar().addMenu('&File')
        newAction = QAction('&New Project', self)
        newAction.setStatusTip('Create a new project.')
        newAction.setShortcut('Ctrl+N')
        newAction.triggered.connect(self.menuNewProject)
        thisMenu.addAction(newAction)
        openAction = QAction('&Open Project', self)
        openAction.setStatusTip('Open an exist project.')
        openAction.setShortcut('Ctrl+O')
        openAction.triggered.connect(self.menuOpenProject)
        thisMenu.addAction(openAction)
        saveAction = QAction('&Save Project', self)
        saveAction.setStatusTip('Save this project to a database file.')
        saveAction.triggered.connect(self.menuSaveProject)
        thisMenu.addSeparator()
        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit this application.')
        exitAction.triggered.connect(qApp.quit)
        thisMenu.addAction(exitAction)

        thisMenu = self.menuBar().addMenu('&Help')
        helpAction = QAction('&Help', self)
        helpAction.setStatusTip('Link to the page on GitHub')
        helpAction.setShortcut('Ctrl+h')
        helpAction.triggered.connect(self.menuHelpAction)
        thisMenu.addAction(helpAction)
        thisMenu.addSeparator()
        aboutAction = QAction('&About...', self)
        aboutAction.setShortcut('Ctrl+A')
        aboutAction.setStatusTip('About this application.')
        aboutAction.triggered.connect(self.menuAboutAction)
        thisMenu.addAction(aboutAction)

        self._windowSize = QSize(1024, 600)
        self.resize(self._windowSize.width(), self._windowSize.height())

        self._formerArea = QScrollArea(self)
        self._nextSampleButton = QPushButton('Next Sample', self)
        self._SameSampleButton = QPushButton('Same Type', self)
        self._DifferentSampleButton = QPushButton('Different Type', self)
        self._newerArea = QScrollArea(self)

        self._menuHeight = 20
        self._formerArea.resize((self.size().width() - 150)/2, self.size().height() - self._menuHeight)
        self._formerArea.move(0, self._menuHeight)
        self._nextSampleButton.resize(150, 25)
        self._nextSampleButton.move((self.size().width() - 150)/2, self._menuHeight)
        self._SameSampleButton.resize(150, 25)
        self._SameSampleButton.move((self.size().width() - 150)/2, self._menuHeight + 35)
        self._DifferentSampleButton.resize(150, 25)
        self._DifferentSampleButton.move((self.size().width() - 150)/2, self._menuHeight + 70)
        self._newerArea.resize((self.size().width() - 150)/2, self.size().height())
        self._newerArea.move((self.size().width() - 150)/2 + 150, self._menuHeight - self._menuHeight)

        self.refreshStatus('Everything is ready.')

        self.show()

    def menuSaveProject(self):
        pass

    def menuNewProject(self):
        newDialog = ProjectDialog()
        newDialog.exec_()
        if newDialog._confirm:
            self._mainProject.former = newDialog._projectInfo['FORMER_IMG']
            self._mainProject.newer = newDialog._projectInfo['NEWER_IMG']
            self._mainProject.databasePath = newDialog._projectInfo['PROJECT_FILE']
            self.refreshStatus('Create project successfully.')

    def refreshStatus(self, tipText):
        self.statusBar().showMessage(tipText)

    def menuOpenProject(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open a exist project file", "",
                                                  "DataBase Files (*.db);;All Files (*)")
        if len(fileName) < 8:
            return
        if fileName[-8:] == '.cdsp.db':
            self._mainProject.databasePath = fileName
            self.refreshStatus('Load project successfully.')
            print(fileName)

    def menuAboutAction(self):
        aboutDialog = AboutDialog()
        aboutDialog.exec_()

    def menuHelpAction(self):
        webbrowser.open('https://github.com/hex-hex/SamplePicker')

    def resizeEvent(self, *args, **kwargs):
        if self._windowSize.width() > self.size().width():
            self.resize(self._windowSize.width(), self.size().height())
        if self._windowSize.height() > self.size().height():
            self.resize(self.size().width(), self._windowSize.height())

        self._formerArea.resize((self.size().width() - 150)/2, self.size().height())
        self._formerArea.move(0, self._menuHeight)
        self._nextSampleButton.resize(150, 25)
        self._nextSampleButton.move((self.size().width() - 150)/2, self._menuHeight)
        self._SameSampleButton.resize(150, 25)
        self._SameSampleButton.move((self.size().width() - 150)/2, self._menuHeight + 35)
        self._DifferentSampleButton.resize(150, 25)
        self._DifferentSampleButton.move((self.size().width() - 150)/2, self._menuHeight + 70)
        self._newerArea.resize((self.size().width() - 150)/2, self.size().height())
        self._newerArea.move((self.size().width() - 150)/2 + 150, self._menuHeight)

    def redjustWiget(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())

