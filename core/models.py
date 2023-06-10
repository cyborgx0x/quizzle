
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, Unicode, String, DateTime, Column, Text
from datetime import datetime
from sqlalchemy import MetaData
from dataclasses import dataclass
import os
basedir = os.path.abspath(os.path.dirname(__file__))
Base = declarative_base()

engine = create_engine('mysql://root:@localhost:3306/quizbank?charset=utf8mb4', echo =True)
Session = sessionmaker(bind=engine)
session = Session()
connection = engine.connect()
meta = MetaData()
@dataclass
class Quizbank(Base):
    question:str
    'quizbank', meta
    __tablename__ = 'quizbank'
    id = Column('id',Integer, primary_key=True)
    question = Column('question',Text)
    solution = Column('solution',Text)
    other_answer_1 = Column('other_answer_1', Text)
    other_answer_2 = Column('other_answer_2', Text)
    other_answer_3 = Column('other_answer_3', Text)
    hint = Column('hint',Text)
    full_solution = Column('full_solution', Text)
    