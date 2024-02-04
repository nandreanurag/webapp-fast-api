from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app import models
from app.database.db import get_db, engine, Base

from app.routers import User, api_router

try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    print("DB connection error ", e)

app = FastAPI()


@app.get("/healthz")
async def root(db: Session = Depends(get_db)):
    try:
        return {"message": "Hello world!!"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))


# app.include_router(User.router)
app.include_router(api_router)

