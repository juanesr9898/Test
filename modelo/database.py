from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

SQLACADEMY_DATABASE_URL = "sqlite:///./base.db"
engine = create_engine(SQLACADEMY_DATABASE_URL, 
                       connect_args={"check_same_thread":False}
                       )
SessionLocal = sessionmaker(bind=engine, autocommit=False,autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
        