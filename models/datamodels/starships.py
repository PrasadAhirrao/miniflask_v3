from pydantic import validator, BaseModel
from models.basemodel import Base
from typing import List, Union, Optional
from pprint import pprint


class Starships(Base):
    starship_id: int
    name: str
    model: str
    manufacturer: str
    cost_in_credits: Union[int, str]
    length: Union[int, float, str]
    max_atmosphering_speed: Union[int, str]
    crew: Union[int, str]
    passengers: Union[int, str]
    cargo_capacity: int
    consumables: str
    hyperdrive_rating: float
    MGLT: int
    starship_class: str

    pilots: Optional[List[str]]
    films: Optional[List[str]]

    @validator("crew")
    def crew_validation(cls, crew):

        if isinstance(crew, str):
            crew_ = ""
            for i in crew:
                if i.isdigit():
                    crew_ += i

            if not crew_:  # returns null if crew doesn't have any digit
                return 'Null'

            return int(crew_)
        elif isinstance(crew, int):
            return crew

    @validator("hyperdrive_rating")
    def hyperdrive_rating_validation(cls, hyperdrive_rating):
        if isinstance(hyperdrive_rating, float):
            return int(hyperdrive_rating)


class ResponseStarships(BaseModel):
    starship_id: int
    name: str
    model: str
    manufacturer: str
    cost_in_credits: Union[int, str]
    length: Union[int, float, str]
    max_atmosphering_speed: Union[int, str]
    crew: Union[int, str]
    passengers: Union[int, str]
    cargo_capacity: int
    consumables: str
    hyperdrive_rating: float
    MGLT: int
    starship_class: str
    created: str
    edited: str
    url: str


if __name__ == "__main__":
    star_data = {
        "name": "Star Destroyer",
        "model": "Imperial I-class Star Destroyer",
        "manufacturer": "Kuat Drive Yards",
        "cost_in_credits": "150000000",
        "length": "1,600",
        "max_atmosphering_speed": "975",
        "crew": "abc",
        "passengers": "n/a",
        "cargo_capacity": "36000000",
        "consumables": "2 years",
        "hyperdrive_rating": "2.0",
        "MGLT": "60",
        "starship_class": "Star Destroyer",
        "pilots": [],
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/"
        ],
        "created": "2014-12-10T15:08:19.848000Z",
        "edited": "2014-12-20T21:23:49.870000Z",
        "url": "https://swapi.dev/api/starships/3/"
    }

    star_obj = Starships(**star_data)
    pprint(dict(star_obj))