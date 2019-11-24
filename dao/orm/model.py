from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class ormAlbum(Base):
    __tablename__ = 'orm_album'
    album_id = Column(Integer, primary_key=True)
    album_title = Column(String(15))
    performer = Column(String(20))

class ormGenre(Base):
    __tablename__ = 'orm_genre'

    genre_id = Column(Integer, primary_key=True)
    genre_name = Column(String(15))
    psychotype = Column(String(15), nullable=False)

class ormStudent(Base):
    __tablename__ = 'orm_student'

    student_id = Column(Integer, primary_key=True)
    faculty = Column(String(20))
    group = Column(String(8))
    name = Column(String(15))
    surname = Column(String(15))
    username = Column(String(32))
