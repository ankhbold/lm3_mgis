__author__ = 'B.Ankhbold'

from sqlalchemy import Column, String, Integer
from .Base import *

class ClPersonRole(Base):

    __tablename__ = 'cl_person_role'

    code = Column(Integer, primary_key=True)
    description = Column(String)
    description_en = Column(String)
