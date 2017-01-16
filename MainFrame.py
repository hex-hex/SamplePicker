import sys
import webbrowser
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from SampleProject import *

class AboutDialog():
    def __init__(self):
        pass

class ProjectDialog():
    def __init__(self):
        pass
    def iniUI(self):
        pass

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('C D S P  by hugh')

        thisMenu = self.menuBar().addMenu('&File')
        newAction = QAction('&New Project', self)
        newAction.setStatusTip('Create a new project.')
        newAction.setShortcut('Ctrl+N')
        thisMenu.addAction(newAction)
        openAction = QAction('&Open Project', self)
        openAction.setStatusTip('Open an exist project.')
        openAction.setShortcut('Ctrl+O')
        thisMenu.addAction(openAction)
        thisMenu.addSeparator()

        exitAction = QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit this application.')
        exitAction.triggered.connect(qApp.quit)
        thisMenu.addAction(exitAction)

        thisMenu = self.menuBar().addMenu('&Help')
        helpAction = QAction('&Help', self)
        helpAction.setStatusTip('Link to my page on GitHub')
        helpAction.setShortcut('Ctrl+h')
        helpAction.triggered.connect(self.menuHelpAction)
        thisMenu.addAction(helpAction)
        thisMenu.addSeparator()
        aboutAction = QAction('&About...', self)
        aboutAction.setShortcut('Ctrl+A')
        aboutAction.setStatusTip('About this application.')
        thisMenu.addAction(aboutAction)

        self._windowSize = QSize(1024, 600)
        self.resize(self._windowSize.width(), self._windowSize.height())

        self._hBox = QHBoxLayout(self)
        self._formerLabel = QLabel()
        self._buttonBox = QVBoxLayout()
        self._newerLabel = QLabel()

        self._currentStatusMessgae = 'Everything is ready.'

        self.statusBar().showMessage(self._currentStatusMessgae)

        self.show()

    def menuHelpAction(self):
        webbrowser.open('https://github.com/hex-hex/SamplePicker')

    def resizeEvent(self, *args, **kwargs):
        if self._windowSize.width() > self.size().width():
            self.resize(self._windowSize.width(), self.size().height())
        if self._windowSize.height() > self.size().height():
            self.resize(self.size().width(), self._windowSize.height())
        print(self.size())

    def redjustWiget(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())

