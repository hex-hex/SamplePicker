import sqlite3
import os
from skimage import io
import numpy as np
import pandas as pd

class Image():
    def __init__(self):
        self.m_filePath = ''
        self.m_imgData = None
        self.m_imgSize = (0, 0, 0)

    @property
    def width(self):
        return self.m_imgSize[1]

    @property
    def height(self):
        return self.m_imgSize[0]

    @property
    def bands(self):
        return self.m_imgSize[2]

    @property
    def file_path(self):
        return self.m_filePath

    @file_path.setter
    def file_path(self, value):
        if os.path.isfile(value):
            self.m_filePath = value
            self.m_imgData = io.imread(value)
            self.m_imgSize = self.m_imgData.shape
        else:
            raise NameError('File does not exist')

    @property
    def file_data(self):
        return self.m_imgData

    def load_img(self):
        self.m_imgData = io.imread(self.m_filePath)

class ProjectSet():
    def __init__(self):
        self.m_formerImg = Image()
        self.m_newerImg = Image()
        self.m_dbPathName = ''
        self.m_listLocation = []
        self.m_sampleSize = 121
        self.m_isEmpty = True

    @property
    def sampleSize(self):
        return self.m_sampleSize

    @sampleSize.setter
    def sampleSize(self, value):
        if value % 2 == 0:
            value = value + 1
        self.m_sampleSize = value

    def width(self):
        return self.m_formerImg.width

    def height(self):
        return self.m_formerImg.height

    def isLoaded(self):
        return not self.m_isEmpty

    def addLocation(self, x, y, isSame):
        self.m_listLocation.append([x, y, isSame])

    @property
    def databasePath(self):
        if len(self.m_dbPathName) != 0:
            return self.m_dbPathName
        else:
            return None

    @databasePath.setter
    def databasePath(self, strFilePath):
        if strFilePath[-8:] == '.cdsp.db':
            self.m_dbPathName = strFilePath
            if not os.path.isfile(strFilePath):
                try:
                    conn = sqlite3.connect(strFilePath)
                    conn.execute('''CREATE TABLE sample_location(index_sample INTEGER PRIMARY KEY autoincrement, row int, column int, isSame int)''')
                    conn.execute('''CREATE TABLE image_path(index_image INTEGER PRIMARY KEY, image_path varchar(255), image_description varchar(255))''')
                    conn.execute('''INSERT INTO image_path(index_image, image_path, image_description) VALUES({0}, '{1}', '{2}')'''.format(
                        0, self.m_formerImg.file_path, 'former image'))
                    conn.execute('''INSERT INTO image_path(index_image, image_path, image_description) VALUES({0}, '{1}', '{2}')'''.format(
                        1, self.m_newerImg.file_path, 'newer image'))
                    #primary key indicates is the image former(0) or newer(1)
                    conn.commit()
                    conn.close()
                    self.m_isEmpty = False
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
                    self.m_isEmpty = False
                    print('Load database successfully.')
                except Exception as e:
                    print(e)

    @property
    def former(self):
        return np.array(self.m_formerImg.file_data)

    @former.setter
    def former(self, strFilePath):
        self.m_formerImg.file_path = strFilePath

    @property
    def newer(self):
        return np.array(self.m_newerImg.file_data)

    @newer.setter
    def newer(self, strFilePath):
        self.m_newerImg.file_path = strFilePath

    def exportDB(self):
        if self.databasePath is not None:
            try:
                conn = sqlite3.connect(self.databasePath)
                for i, sample in enumerate(self.m_listLocation):
                    conn.execute('''INSERT INTO sample_location(row, column, IsSame) VALUES({0},{1},{2})'''.format(
                                sample[0], sample[1], sample[2]))
                conn.commit()
                self.databasePath = []
                print('Export data successfully')
                conn.close()
            except Exception as e:
                print(e)

    def getDB(self):
        try:
            conn = sqlite3.connect(self.databasePath)
            content = conn.execute('''SELECT * FROM sample_location''')
            content = content.fetchall()
            conn.close()
        except Exception as e:
            print(e)

        return content


