__author__ = 'B.Ankhbold'

from sqlalchemy import Column, String, Integer
from .Base import *

class ClMortgageType(Base):

    __tablename__ = 'cl_mortgage_type'

    code = Column(Integer, primary_key=True)
    description = Column(String)
    description_en = Column(String)
