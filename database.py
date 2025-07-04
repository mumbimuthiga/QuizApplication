from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



URL_DATABASE='postgresql://postgres:mumbi%40123@localhost:5433/QuizApplication'

engine=create_engine(URL_DATABASE)
SessionLocal=sessionmaker(autocommit=False ,autoflush=False,bind=engine)
Base=declarative_base()