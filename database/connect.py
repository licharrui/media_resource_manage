from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from travel_of_the_life.config import CONFIG

SQLALCHEMY_DATABASE_URL = f"mysql://{CONFIG.data_base.user}:{CONFIG.data_base.password}@{CONFIG.data_base.ip}/{CONFIG.data_base.db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
