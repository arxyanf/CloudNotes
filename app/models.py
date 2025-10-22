from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    
    id = column(Integer, primary_key=True)
    title = column(String)
    content = column(String)
    
    

