from pydantic import BaseModel, validator
from models.basemodel import Base
from typing import List, Union, Optional
from pprint import pprint


class Planets(Base):
    planet_id: int
    name: str
    rotation_period: int
    orbital_period: int
    diameter: int
    climate: str
    gravity: str
    terrain: str
    surface_water: Union[int, str]
    population: Union[int, str]

    residents: Optional[List[str]]
    films: Optional[List[str]]

    @validator("population")
    def check_population(cls, population):
        if isinstance(population, str):
            return None

class ResponsePlanets(BaseModel):
    planet_id: int
    name: str
    rotation_period: int
    orbital_period: int
    diameter: int
    climate: str
    gravity: str
    terrain: str
    created: str
    edited: str
    url: str
    surface_water: Union[int, str]
    population: Union[int, str]


if __name__ == "__main__":
    pl_data = {
        "name": "Tatooine",
        "rotation_period": "23",
        "orbital_period": "304",
        "diameter": "10465",
        "climate": "arid",
        "gravity": "1 standard",
        "terrain": "desert",
        "surface_water": "1",
        "population": "200000",
        "residents": [
            "https://swapi.dev/api/people/1/",
            "https://swapi.dev/api/people/2/",
            "https://swapi.dev/api/people/4/",
            "https://swapi.dev/api/people/6/",
            "https://swapi.dev/api/people/7/",
            "https://swapi.dev/api/people/8/",
            "https://swapi.dev/api/people/9/",
            "https://swapi.dev/api/people/11/",
            "https://swapi.dev/api/people/43/",
            "https://swapi.dev/api/people/62/"
        ],
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/4/",
            "https://swapi.dev/api/films/5/",
            "https://swapi.dev/api/films/6/"
        ],
        "created": "2014-12-09T13:50:49.641000Z",
        "edited": "2014-12-20T20:58:18.411000Z",
        "url": "https://swapi.dev/api/planets/1/"
    }

    pl_obj = Planets(**pl_data)
    pprint(dict(pl_obj))