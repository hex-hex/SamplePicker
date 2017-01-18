import sqlite3
import os
from skimage import io

class Image():
    def __init__(self):
        self._filePath = ''
        self._imgData = None
        self._imgSize = (0, 0, 0)

    @property
    def width(self):
        return self._imgSize[0]

    @property
    def height(self):
        return self._imgSize[1]

    @property
    def bands(self):
        return self._imgSize[2]

    @property
    def file_path(self):
        pass

    @file_path.setter
    def file_path(self, value):
        if os.path.isfile(value):
            self._filePath = value
            self._imgData = io.imread(value)
            self._imgSize = self._imgData.shape
        else:
            raise NameError('File does not exist')

    @property
    def file_data(self):
        pass

    def load_img(self):
        self._imgData = io.imread(self._filePath)


class ProjectSet():
    def __init__(self):
        self._formerImg = Image()
        self._newerImg = Image()

    @property
    def former(self):
        pass

    @former.setter
    def former(self, strFilePath):
        self._formerImg.file_path = strFilePath

    @property
    def newer(self):
        pass

    @newer.setter
    def newer(self, strFilePath):
        self._newerImg.file_path = strFilePath

    def load_img(self):
        pass

    def exportDB(self):
        pass