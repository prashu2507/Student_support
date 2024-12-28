from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for ORM models
Base = declarative_base()

# Database models
class ClassTiming(Base):
    __tablename__ = 'class_timings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String, nullable=False)
    time = Column(String, nullable=False)
    day = Column(String, nullable=False)

class Assignment(Base):
    __tablename__ = 'assignments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String, nullable=False)
    due_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)

class Exam(Base):
    __tablename__ = 'exams'
    id = Column(Integer, primary_key=True, autoincrement=True)
    subject = Column(String, nullable=False)
    exam_date = Column(Date, nullable=False)
    preparation_notes = Column(String, nullable=True)

# Database setup
DATABASE_URL = "sqlite:///student_support.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables
Base.metadata.create_all(engine)
