from app.api.database import Base
from sqlalchemy import Column, Integer, String

class user(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    class Config:
        from_attributes = True