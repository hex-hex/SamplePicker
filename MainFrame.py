import sys
import webbrowser
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from SampleProject import *
from ProjectDialog import *
from AboutDialog import *

class MainApp(QMainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.m_currentLocation = np.array([0, 0])

        self.setWindowTitle('C D S P  by hugh')
        self.m_mainProject = ProjectSet()
        self.m_menuHeight = 20

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

        self.m_windowSize = QSize(1024, 600)

        self.m_formerArea = QScrollArea(self)
        self.m_formerView = QLabel()
        self.m_formerArea.setWidget(self.m_formerView)
        self.m_formerArea.horizontalScrollBar().sliderMoved.connect(self.onFormerHorizontalMoved)
        self.m_formerArea.verticalScrollBar().sliderMoved.connect(self.onFormerVerticalMoved)

        self.m_newerArea = QScrollArea(self)
        self.m_newerView = QLabel()
        self.m_newerArea.setWidget(self.m_newerView)
        self.m_newerArea.horizontalScrollBar().sliderMoved.connect(self.onNewerHorizontalMoved)
        self.m_newerArea.verticalScrollBar().sliderMoved.connect(self.onNewerVerticalMoved)

        self.m_formerWindow = QLabel(self)
        self.m_formerWindow.resize(self.m_mainProject.sampleSize, self.m_mainProject.sampleSize)
        self.m_newerWindow = QLabel(self)
        self.m_newerWindow.resize(self.m_mainProject.sampleSize, self.m_mainProject.sampleSize)


        self.m_nextSampleButton = QPushButton('Next Sample', self)
        self.m_nextSampleButton.resize(150, 25)
        self.m_nextSampleButton.clicked.connect(self.onNextButton)
        self.m_DifferentSampleButton = QPushButton('Different Type', self)
        self.m_DifferentSampleButton.resize(150, 25)
        self.m_DifferentSampleButton.clicked.connect(self.onDifferentButton)
        self.m_SameSampleButton = QPushButton('Same Type', self)
        self.m_SameSampleButton.resize(150, 25)
        self.m_SameSampleButton.clicked.connect(self.onSameButton)

        self.resize(self.m_windowSize.width(), self.m_windowSize.height())
        self.refreshStatus('Everything is ready.')
        self.show()

    def randWindow(self):
        halfWindow = np.floor(self.m_mainProject.sampleSize / 2).astype(int)
        randLocation = np.array([np.random.rand() * self.m_mainProject.width(),
                                 np.random.rand() * self.m_mainProject.height()])
        randLocation = np.floor(randLocation).astype(int)
        if (randLocation[0] - halfWindow < 0 or
            randLocation[0] + halfWindow + 1 > self.m_mainProject.width() or
            randLocation[1] - halfWindow < 0 or
            randLocation[1] + halfWindow + 1 > self.m_mainProject.height()):
            return  self.randWindow()
        else:
            gridWindow = np.meshgrid(
                np.array(randLocation[0] - halfWindow,
                         randLocation[0] + halfWindow),
                np.array(randLocation[1] - halfWindow,
                         randLocation[1] + halfWindow)
            )
            pixelCount = self.m_mainProject.sampleSize ** 2
            gridWindow = np.hstack((gridWindow[0].reshape(pixelCount, 1),
                                    gridWindow[1].reshale(pixelCount, 1)))
            gridWindow = np.delete(gridWindow, np.ceil(pixelCount / 2), axis=0)

            formerImageWindow = self.m_mainProject.former[randLocation[0] - halfWindow:randLocation[0] + halfWindow + 1,
                                randLocation[1] - halfWindow:randLocation[1] + halfWindow + 1]

            newerImageWindow = self.m_mainProject.newer[randLocation[0] - halfWindow:randLocation[0] + halfWindow + 1,
                                randLocation[1] - halfWindow:randLocation[1] + halfWindow + 1]

            return randLocation, formerImageWindow, newerImageWindow, gridWindow

    def onNextButton(self):
        sampleLocation, formerWindow, newerWindow = self.randWindow()

    def onDifferentButton(self):
        pass
    def onSameButton(self):
        pass

    def onFormerHorizontalMoved(self):
        self.m_newerArea.horizontalScrollBar().setValue(self.m_formerArea.horizontalScrollBar().value())

    def onFormerVerticalMoved(self):
        self.m_newerArea.verticalScrollBar().setValue(self.m_formerArea.verticalScrollBar().value())

    def onNewerHorizontalMoved(self):
        self.m_formerArea.horizontalScrollBar().setValue(self.m_newerArea.horizontalScrollBar().value)

    def onNewerVerticalMoved(self):
        self.m_formerArea.verticalScrollBar().setValue(self.m_newerArea.verticalScrollBar().value())

    def menuSaveProject(self):
        pass

    def menuNewProject(self):
        newDialog = ProjectDialog()
        newDialog.exec_()
        if newDialog._confirm:
            self.m_mainProject.former = newDialog._projectInfo['FORMER_IMG']
            self.m_mainProject.newer = newDialog._projectInfo['NEWER_IMG']
            self.m_mainProject.databasePath = newDialog._projectInfo['PROJECT_FILE']
            self.loadImages()
            self.refreshStatus('Create project successfully.')

    def refreshStatus(self, tipText):
        self.statusBar().showMessage(tipText)

    def menuOpenProject(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open a exist project file", "",
                                                  "DataBase Files (*.db);;All Files (*)")
        if len(fileName) < 8:
            return
        if fileName[-8:] == '.cdsp.db':
            self.m_mainProject.databasePath = fileName
            self.loadImages()
            self.refreshStatus('Load project successfully.')

    def loadImages(self):
        if self.m_mainProject.isLoaded():
            try:
                npImg = self.m_mainProject.former
                image = QImage(npImg.data, npImg.shape[1], npImg.shape[0], npImg.shape[1] * 3, QImage.Format_RGB888)
                self.m_formerView.setPixmap(QPixmap(image))
                self.m_formerView.resize(self.m_mainProject.width(), self.m_mainProject.height())
                npImg = self.m_mainProject.newer
                image = QImage(npImg.data, npImg.shape[1], npImg.shape[0], npImg.shape[1] * 3, QImage.Format_RGB888)
                self.m_newerView.setPixmap(QPixmap(image))
                self.m_newerView.resize(self.m_mainProject.width(), self.m_mainProject.height())
            except Exception as e:
                print(e)

    def menuAboutAction(self):
        aboutDialog = AboutDialog()
        aboutDialog.exec_()

    def menuHelpAction(self):
        webbrowser.open('https://github.com/hex-hex/SamplePicker')

    def resizeEvent(self, *args, **kwargs):
        if self.m_windowSize.width() > self.size().width():
            self.resize(self.m_windowSize.width(), self.size().height())
        if self.m_windowSize.height() > self.size().height():
            self.resize(self.size().width(), self.m_windowSize.height())

        self.m_nextSampleButton.move((self.size().width() - 150)/2, self.m_menuHeight)
        self.m_SameSampleButton.move((self.size().width() - 150)/2, self.m_menuHeight + 35)
        self.m_DifferentSampleButton.move((self.size().width() - 150)/2, self.m_menuHeight + 70)

        self.m_formerArea.resize((self.size().width() - 150)/2, self.size().height() - self.m_menuHeight * 2)
        self.m_formerArea.move(0, self.m_menuHeight)
        self.m_newerArea.resize((self.size().width() - 150)/2, self.size().height() - self.m_menuHeight * 2)
        self.m_newerArea.move((self.size().width() - 150)/2 + 150, self.m_menuHeight)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainApp()
    sys.exit(app.exec_())

