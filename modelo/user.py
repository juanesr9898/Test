from sqlalchemy import Column, Integer, String
from modelo.database import Base
from sqlalchemy.orm import relationship, Session

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    email = Column(String)
