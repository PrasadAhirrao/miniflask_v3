from models.basemodel import Base
from typing import List, Union, Optional
from pprint import pprint
from pydantic import validator, BaseModel


class Species(Base):
    species_id: int
    name: str
    classification: str
    designation: str
    average_height: Union[int, str]
    skin_colors: str
    hair_colors: str
    eye_colors: str
    average_lifespan: Union[int, str]
    homeworld: Optional[str]

    people: Optional[List[str]]
    films: Optional[List[str]]

    # @validator("homeworld")
    # def validate_homeworld(cls, homeworld):
    #     breakpoint()
    #     if homeworld is None:
    #         cls.homeworld = 'Null'
    #     return homeworld


class ResponseSpecies(BaseModel):
    species_id: int
    name: str
    classification: str
    designation: str
    average_height: Union[int, str]
    skin_colors: str
    hair_colors: str
    eye_colors: str
    average_lifespan: Union[int, str]
    homeworld: Optional[str]
    created: str
    edited: str
    url: str


if __name__ == "__main__":
    speci_data = {
        "name": "Human",
        "classification": "mammal",
        "designation": "sentient",
        "average_height": "180",
        "skin_colors": "caucasian, black, asian, hispanic",
        "hair_colors": "blonde, brown, black, red",
        "eye_colors": "brown, blue, green, hazel, grey, amber",
        "average_lifespan": "120",
        "homeworld": "https://swapi.dev/api/planets/9/",
        "language": "Galactic Basic",
        "people": [
            "https://swapi.dev/api/people/66/",
            "https://swapi.dev/api/people/67/",
            "https://swapi.dev/api/people/68/",
            "https://swapi.dev/api/people/74/"
        ],
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/4/",
            "https://swapi.dev/api/films/5/",
            "https://swapi.dev/api/films/6/"
        ],
        "created": "2014-12-10T13:52:11.567000Z",
        "edited": "2014-12-20T21:36:42.136000Z",
        "url": "https://swapi.dev/api/species/1/"
    }

    speci_obj = Species(**speci_data)
    pprint(dict(speci_obj))