from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from database import Base,engine,SessionLocal
import crud
from models import Base
from schemas import FeatureCollection


Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/polygontocenterline/")
async def polygonToCenterLine(db: Session = Depends(get_db)):
    resp = crud.get_centerline(db)
    return resp


@app.post("/createPolygon")
async def createPolygon(db: Session = Depends(get_db),polygon:FeatureCollection = None):
    json_data = jsonable_encoder(polygon.dict())
    return crud.create_polygon(db,polygon=json_data)