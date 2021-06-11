from sqlalchemy import Column, Integer, String, DateTime
from modelo.database import Base
from datetime import datetime

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    color = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    