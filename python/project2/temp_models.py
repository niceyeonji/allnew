from sqlalchemy import Column, TEXT, INT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Temp(Base):
    __tablename__ = "temp"

    DATADATE = Column(TEXT, nullable=False, primary_key=True)
    TEMP_AVR = Column(INT, nullable=False)

