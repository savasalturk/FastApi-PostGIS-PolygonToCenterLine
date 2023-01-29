from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from database import Base


class CenterLine(Base):
    __tablename__ = 'centerline'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    geom = Column(Geometry('POLYGON',srid=4326,from_text='ST_GeomFromText'))