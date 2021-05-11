import random
import string
from typing import Optional

# from schemas import city
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
from models import CityModels
from schemas import CitySchemas

router = APIRouter()


@router.post("/cities")
async def city(request_city: CitySchemas.CitySchema, db: Session = Depends(database.get_db)):
    cityObj = CityModels.CityModel(name=request_city.name, string=get_random_string())
    db.add(cityObj)
    db.commit()
    return cityObj


def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.sample(letters, 6))
    print(result_str)
    return result_str


@router.get("/cities")
def getCities(id: Optional[int] = None, db: Session = Depends(database.get_db)):
    if id is None:
        city = db.query(CityModels).all()
    else:
        city = db.query(CityModels.CityModel).filter(CityModels.CityModel.id == id).first()

    return city

