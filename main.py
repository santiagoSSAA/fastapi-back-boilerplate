import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/health")
async def health_check():
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        return {"status": "healthy"}
    except SQLAlchemyError:
        return {"status": "unhealthy"}
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI"}
