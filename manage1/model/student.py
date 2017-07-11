"""Student model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from manage1.model.meta import Base


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(100))

    def __init__(self, name='', email='', password=''):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<Student('%s')" % self.name
