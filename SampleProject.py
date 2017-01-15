import sqlite3
from skimage import io
class Image():
    def __init__(self):
        self._filePath = ''

    @property
    def file_path(self):
        pass
    @file_path.setter
    def file_path(self, value):
        self._filePath = value

    @property
    def file_data(self):
        pass

    def load_img(self):
        pass


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