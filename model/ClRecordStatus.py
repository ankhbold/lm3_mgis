__author__ = 'B.Ankhbold'

from sqlalchemy import Column, String, Integer
from .Base import *

class ClRecordStatus(Base):

    __tablename__ = 'cl_record_status'

    code = Column(Integer, primary_key=True)
    description = Column(String)
    description_en = Column(String)
