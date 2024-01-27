from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db

# try:
#     models.Base.metadata.create_all(bind=engine)
# except Exception as e:
#     print("DB connection error ", e)

app = FastAPI()

@app.get("/healthz")
async def root(db: Session = Depends(get_db)):
    try:
        return {"message": "Hello world!!"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))