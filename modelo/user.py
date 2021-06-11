from sqlalchemy import Column, Integer, String
from modelo.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    email = Column(String)
    password = Column(String)
