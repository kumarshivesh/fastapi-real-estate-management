from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()  

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

print(f"DATABASE_URL: {SQLALCHEMY_DATABASE_URL}")  # Add this line to verify

if SQLALCHEMY_DATABASE_URL is None:
    raise ValueError("No DATABASE_URL found in environment variables")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
