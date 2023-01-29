from typing import List
from pydantic import BaseModel


class Properties(BaseModel):
    name: str


class Geometry(BaseModel):
    # polygon
    coordinates: List[List[List[float]]]
    type: str


class Feature(BaseModel):
    type: str
    properties: Properties
    geometry: Geometry


class FeatureCollection(BaseModel):
    type: str
    features: List[Feature]

    class Config:
        orm_mode = True