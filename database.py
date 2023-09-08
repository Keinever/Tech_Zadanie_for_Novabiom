from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

from config import DB_NAME, DB_PORT, DB_HOST, DB_PASS, DB_USER

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base: DeclarativeMeta = declarative_base()


class ResultTable(Base):
    __tablename__ = 'result_table'

    id = Column(Integer, primary_key=True)
    taxonname = Column(String, nullable=False)
    composition = Column(String, nullable=False)
    change_in_abundance = Column(String, nullable=False)
    frequency = Column(String, nullable=False)
    additive_type = Column(String, nullable=False)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
