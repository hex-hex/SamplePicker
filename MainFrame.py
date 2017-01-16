import sys
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
        thisMenu.addAction(QAction('&Help', self))
        thisMenu.addSeparator()
        thisMenu.addAction(QAction('&About...', self))

        self._windowSize = [600, 400]
        self.resize(self._windowSize[0], self._windowSize[1])

        self._currentStatusMessgae = 'Everything is ready.'

        self.statusBar().showMessage(self._currentStatusMessgae)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())

