# Author: OMKAR PATHAK (Improved Version)

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
import os

# Use configurable DB path
DB_URL = os.getenv("DB_URL", "sqlite:///example.db")

engine = create_engine(DB_URL, echo=True)
Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    university = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(username={self.username}, name={self.firstname} {self.lastname})>"


def create_tables():
    Base.metadata.create_all(engine)


def main():
    create_tables()

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create object
        user = Student('OmkarPathak', 'Omkar', 'Pathak', 'MIT')
        session.add(user)
        session.commit()

        # Query
        students = session.query(Student).order_by(Student.id).all()
        for student in students:
            print(student.firstname, student.lastname)

    except Exception as e:
        print("Error:", e)
        session.rollback()

    finally:
        session.close()


if __name__ == '__main__':
    main()
