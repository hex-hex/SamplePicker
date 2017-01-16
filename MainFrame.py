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
        thisMenu.addAction(QAction('&New Project', self))
        thisMenu.addAction(QAction('&Open Project', self))
        thisMenu.addSeparator()
        thisMenu.addAction(QAction('&Exit', self))

        thisMenu = self.menuBar().addMenu('&Help')
        thisMenu.addAction(QAction('&Help', self))
        thisMenu.addSeparator()
        thisMenu.addAction(QAction('&About...', self))

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())

