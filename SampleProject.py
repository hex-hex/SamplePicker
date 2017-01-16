import sqlite3
import os
from skimage import io

class Image():
    def __init__(self):
        self._filePath = ''
        self._imgData = None

    @property
    def file_path(self):
        pass

    @file_path.setter
    def file_path(self, value):
        if os.path.isfile(value):
            self._filePath = value
        else:
            raise NameError('File does not exist')

    @property
    def file_data(self):
        pass

    def load_img(self):
        self._imgData = io.imread(self._filePath)


class ProjectSet():
    def __init__(self):
        pass

    @property
    def former(self):
        pass

    @property
    def newer(self):
        pass


    def load_img(self):
        pass

    def exportDB(self):
        pass