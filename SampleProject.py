import sqlite3
import os
from skimage import io
import numpy as np
import pandas as pd

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
        return self._filePath

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
        return self._imgData

    def load_img(self):
        self._imgData = io.imread(self._filePath)

class ProjectSet():
    def __init__(self):
        self._formerImg = Image()
        self._newerImg = Image()
        self._dbPathName = ''
        self._listLocation = []
        self._sampleSize = 49

    def addLocation(self, x, y, isSame):
        self._listLocation.append([x, y, isSame])

    @property
    def databasePath(self):
        if len(self._dbPathName) != 0:
            return self
        else:
            return None

    @databasePath.setter
    def databasePath(self, strFilePath):
        if strFilePath[-8:] == '.cdsp.db':
            self._dbPathName = strFilePath
            if not os.path.isfile(strFilePath):
                try:
                    conn = sqlite3.connect(strFilePath)
                    conn.execute('''CREATE TABLE sample_location(index_sample INTEGER PRIMARY KEY autoincrement, row int, column int, isSame int)''')
                    conn.execute('''CREATE TABLE image_path(index_image INTEGER PRIMARY KEY, image_path varchar(255), image_description varchar(255))''')
                    conn.execute('''INSERT INTO image_path(index_image, image_path, image_description) VALUES({0}, '{1}', '{2}')'''.format(
                        0, self._formerImg.file_path, 'former image'))
                    conn.execute('''INSERT INTO image_path(index_image, image_path, image_description) VALUES({0}, '{1}', '{2}')'''.format(
                        1, self._newerImg.file_path, 'newer image'))
                    #primary key indicates is the image former(0) or newer(1)
                    conn.commit()
                    conn.close()
                    print('Create database successfully.')
                except Exception as e:
                    print(e)
            else:
                try:
                    conn = sqlite3.connect(strFilePath)
                    content = conn.execute('''SELECT * FROM image_path WHERE index_image = 0''')
                    imageFormerInfo = content.fetchone()
                    self.former = imageFormerInfo[1]
                    content = conn.execute('''SELECT * FROM image_path WHERE index_image = 1''')
                    imageNewerInfo = content.fetchone()
                    self.newer = imageNewerInfo[1]
                    conn.close()
                    print('Load database successfully.')
                except Exception as e:
                    print(e)

    @property
    def former(self):
        return self._formerImg.file_data

    @former.setter
    def former(self, strFilePath):
        self._formerImg.file_path = strFilePath

    @property
    def newer(self):
        return self._newerImg.file_data

    @newer.setter
    def newer(self, strFilePath):
        self._newerImg.file_path = strFilePath

    def exportDB(self):
        if self.databasePath is not None:
            try:
                conn = sqlite3.connect(self.databasePath)
                for i, sample in enumerate(self._listLocation):
                   conn.execute('''INSERT INTO sample_location(row, column, IsSame) VALUES({0},{1},{2})'''.format(
                                sample[0][0], sample, sample[0][1], sample[1]))
                conn.commit()
                self.databasePath = []
                print('Export data successfully')
            except Exception as e:
                print(e)

    def getDB(self):
        self.exportDB()
        pass

