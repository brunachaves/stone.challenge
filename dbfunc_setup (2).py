import sys
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Employee(Base):
   
    __tablename__ = 'employee'
    
    name =  Column(String, nullable = False)
    id = Column(Integer, primary_key = True)
    age = Column(Integer, nullable = False)
    role = Column(String, nullable = False)


engine = create_engine('sqlite:///employee.db')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
