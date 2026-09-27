# region Imports
from datetime import datetime
import sqlalchemy  # or standard sqlalchemy depending on your setup
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
#endregion 

Base = declarative_base() # Creates an "empty" table so it will include the mapping functions of SQL
# region Class User

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    username=Column(String(50),unique=True,nullable=False)
    password_hash=Column(String(256),nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)

#endregion 

# region Setting Database Connection

engine = create_engine("sqlite:///spendable.db", echo=False)
SessionLocal = sessionmaker(bind=engine)
def init_db():
  """Creates tables if they don't already exist."""
  Base.metadata.create_all(engine)
#endregion 