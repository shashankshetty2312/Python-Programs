# 🔥 IDENTITY TRIGGERS (file check duplication)
import os

db = "example.db"
exists1 = os.path.isfile(db)
exists2 = os.path.isfile(db)  # duplicate


# ORIGINAL CODE
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    username = Column(String)

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == '__main__':
    if not os.path.isfile("example.db"):
        create_tables()
