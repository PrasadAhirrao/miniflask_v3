from pydantic import BaseModel
from models.basemodel import Base
from typing import List, Optional, Union
from pprint import pprint


class Vehicles(Base):
    vehicle_id: int
    cargo_capacity: Union[int, str]
    consumables: str
    cost_in_credits: Union[int, str]
    crew: int
    length: Union[int, float]
    manufacturer: str
    max_atmosphering_speed: int
    model: str
    name: str
    passengers: int
    vehicle_class: str

    pilots: Optional[List[str]]
    films: Optional[List[str]]


class ResponseVehicles(BaseModel):
    vehicle_id: int
    cargo_capacity: Union[int, str]
    consumables: str
    cost_in_credits: Union[int, str]
    crew: int
    length: Union[int, float]
    manufacturer: str
    max_atmosphering_speed: int
    model: str
    name: str
    passengers: int
    vehicle_class: str
    created: str
    edited: str


if __name__ == "__main__":
    vehicles_data = {
            "cargo_capacity":  "none",  # "50000",
            "consumables": "2 months",
            "cost_in_credits": "150000",
            "created": "2014-12-10T15:36:25.724000Z",
            "crew": "46",
            "edited": "2014-12-10T15:36:25.724000Z",
            "length": "36.8",
            "manufacturer": "Corellia Mining Corporation",
            "max_atmosphering_speed": "30",
            "model": "Digger Crawler",
            "name": "Sand Crawler",
            "passengers": "30",
            "pilots": [],
            "films": [
                "https://swapi.dev/api/films/1/"
            ],
            "url": "https://swapi.dev/api/vehicles/4/",
            "vehicle_class": "wheeled"
        }

    vehi_obj = Vehicles(**vehicles_data)
    pprint(dict(vehi_obj))