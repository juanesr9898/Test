from sqlalchemy import Column, Integer, String
from modelo.database import Base
from sqlalchemy.orm import relationship, Session

class Token(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String)
    expire = Column(Integer)
    
