__author__ = 'B.Ankhbold'

from sqlalchemy import Column, String, Integer
from .Base import *

class ClBank(Base):

    __tablename__ = 'cl_bank'

    code = Column(Integer, primary_key=True)
    description = Column(String)
    description_en = Column(String)
