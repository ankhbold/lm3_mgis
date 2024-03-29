__author__ = 'B.Ankhbold'
#!/usr/bin/python
# -*- coding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

class FileUtils(object):

    @staticmethod
    def temp_file_path():
        path = QDir.tempPath()

        if not QDir(path).exists():
            QDir().mkpath(path)

        return path

    @staticmethod
    def map_file_path():

        map_path = os.path.join(os.path.dirname(__file__), "../view/map/")

        return str(map_path)


