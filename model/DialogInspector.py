__author__ = 'B.Ankhbold'
# !/usr/bin/python
# -*- coding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from ..model.Singleton import Singleton

class DialogInspector(QObject):

    __metaclass__ = Singleton

    def __init__(self, parent=None):

        super(QObject, self).__init__(parent)
        self.dialog_is_visible = False

    def dialog_visible(self):

        return self.dialog_is_visible

    def set_dialog_visible(self, visible):

        self.dialog_is_visible = visible

