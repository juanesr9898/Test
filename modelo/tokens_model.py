from sqlalchemy import Column, Integer, String, DateTime
from modelo.database import Base

class Token(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True, index=True)
    sub = Column(String)
    token = Column(String)
    creation = Column(DateTime)
    expire = Column(DateTime)
    
