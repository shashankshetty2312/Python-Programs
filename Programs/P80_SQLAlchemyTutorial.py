from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///db.db')
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, n):   # 🔥 Trigger 1: short param
        self.name = n


def create():
    Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)  # 🔥 Trigger 2: duplicate


# 🔥 Trigger 3: missing session
