# Author: OMKAR PATHAK (Refactored & Improved)

from sqlalchemy import create_engine, String, Integer, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker
)
import os

# -----------------------------
# Database Configuration
# -----------------------------
DATABASE_URL = "sqlite:///example.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,          # Logs SQL queries (use False in production)
    future=True
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# -----------------------------
# Base Class (SQLAlchemy 2.0)
# -----------------------------
class Base(DeclarativeBase):
    pass


# -----------------------------
# Model Definition
# -----------------------------
class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(50), nullable=False)
    lastname: Mapped[str] = mapped_column(String(50), nullable=False)
    university: Mapped[str] = mapped_column(String(100), nullable=True)

    def __repr__(self):
        return (
            f"Student(id={self.id}, username='{self.username}', "
            f"name='{self.firstname} {self.lastname}', university='{self.university}')"
        )


# -----------------------------
# Utility Functions
# -----------------------------
def init_db():
    """Create database tables"""
    Base.metadata.create_all(bind=engine)


def get_session():
    """Get DB session (context manager safe)"""
    return SessionLocal()


def create_student(session, username, firstname, lastname, university):
    """Insert new student"""
    student = Student(
        username=username,
        firstname=firstname,
        lastname=lastname,
        university=university
    )
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


def get_all_students(session):
    """Fetch all students"""
    stmt = select(Student).order_by(Student.id)
    return session.execute(stmt).scalars().all()


# -----------------------------
# Main Execution
# -----------------------------
def main():
    if not os.path.exists("example.db"):
        init_db()

    with get_session() as session:
        # Create a new student
        student = create_student(
            session,
            username="OmkarPathak",
            firstname="Omkar",
            lastname="Pathak",
            university="MIT"
        )
        print("Inserted:", student)

        # Fetch all students
        students = get_all_students(session)
        print("\nAll Students:")
        for s in students:
            print(s)


if __name__ == "__main__":
    main()
