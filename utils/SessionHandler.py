__author__ = 'B.Ankhbold'
# !/usr/bin/python
# -*- coding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from ..model.Singleton import Singleton
from ..model.SetRole import SetRole
from ..model.Constants import *

class SessionHandler(QObject):

    __metaclass__ = Singleton

    session_static = None

    def __init__(self, parent=None):

        super(QObject, self).__init__(parent)
        self.parent = parent
        self.session = None
        self.engine = None
        self.password = None

    def current_password(self):

        return self.password

    def session_instance(self):

        return SessionHandler.session_static
        # return 1

    def get_connection(self):

        connection = self.engine.connect()
        return connection

    # @property
    def create_session(self, user, password, host, port, database):

        if SessionHandler.session_static is not None:
            SessionHandler.session_static.close()

        # try:
        self.engine = create_engine("postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database))
        self.password = password
        Session = sessionmaker(bind=self.engine)
        SessionHandler.session_static = Session()

        SessionHandler.session_static.autocommit = False
        SessionHandler.session_static.execute(set_search_path)

        set_role_count = SessionHandler.session_static.query(SetRole).filter(SetRole.user_name == user).filter(
            SetRole.is_active == True).count()

        if set_role_count == 0:
            QMessageBox.information(None, self.tr("Connection Error"),
                                    self.tr("The user name {0} is not registered.").format(user))
            self.session = None
            self.engine = None
            self.password = None
            return False

        setRole = SessionHandler.session_static.query(SetRole).filter(SetRole.user_name == user).filter(SetRole.is_active == True).one()
        auLevel2List = setRole.restriction_au_level2.split(",")
        schemaList = []

        for auLevel2 in auLevel2List:
            auLevel2 = auLevel2.strip()
            schemaList.append("s" + auLevel2)

        SessionHandler.session_static.execute(set_search_path)
        SessionHandler.session_static.commit()

        return True

        # except SQLAlchemyError:
        #     self.session = None
        #     self.engine = None
        #     self.password = None
        #     raise

    def destroy_session(self):

        if SessionHandler.session_static is not None:
            SessionHandler.session_static.close()
            SessionHandler.session_static = None