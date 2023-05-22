from sqlalchemy import Column, TEXT, INT, DOUBLE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Temp(Base):
    __tablename__ = "temp"

    Average_tem = Column(DOUBLE, nullable=False)
    monthly = Column(TEXT, nullable=False, primary_key=True)

class Fire(Base):
    __tablename__ = "Firedb"

    Firecount = Column(INT, nullable=False)
    yearmonth = Column(TEXT, nullable=False, primary_key=True)