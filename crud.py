from sqlalchemy.orm import Session
from sqlalchemy import func, select
import models
from shapely.geometry import shape


def get_centerline(db: Session):
    query = """SELECT
                json_build_object(
                                'type', 'FeatureCollection',
                                'features', json_agg(ST_AsGeoJSON(t.*)::json)
                                )
                FROM
                (
                SELECT
                  id,
                  name,
                  ST_AsEWKT((st_dump(ST_ApproximateMedialAxis(geom)::geometry)).geom)::geometry AS geom
                FROM
                  centerline c) AS t ;"""
    
    data = db.execute(query).fetchone()["json_build_object"]
    return data


def create_polygon(db: Session, polygon: dict):
    for i in polygon["features"]:
      geom = shape(i["geometry"]).wkt
      db_polygon = models.CenterLine(name=i["properties"]["name"],geom = geom)
      db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return {"message":"success"}
