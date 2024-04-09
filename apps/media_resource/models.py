from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.connect import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_online = Column(Boolean, default=False)
    resources = relationship("Resource", back_populates="owner")


class Resource(Base):
    __tablename__ = "resource"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    file_path = Column(String, unique=True)
    file_name = Column(String, unique=True)
    file_type = Column()
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="resources")
