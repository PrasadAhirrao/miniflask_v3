"""

http://127.0.0.1:5000/tasks/taskone
http://127.0.0.1:5000/tasks/tasktwo
http://127.0.0.1:5000/tasks/taskthree
http://127.0.0.1:5000/tasks/taskfour

"""

import requests
from flask import Blueprint, jsonify, Response, json
from utils.randgen import ProduceChars
from datetime import datetime
from multiprocessing.pool import ThreadPool
from typing import List, Dict
from utils.fetch_data import fetch_data
from models.datamodels.films import Films as Films
from models.datamodels.characters import Characters
from models.datamodels.planets import Planets
from models.datamodels.vehicles import Vehicles
from models.datamodels.species import Species
from models.datamodels.starships import Starships
from models.dal.dml import insert_resource

swapi = Blueprint("starwars", __name__, url_prefix="/tasks")


@swapi.route("/taskone")
def task_one():
    """
    The Star Wars API lists 82 main characters in the Star Wars saga.
    This app uses a random number generator that picks a number between 1-82.
    Using these random numbers it will be pulling 15 characters from the API using Python.
    """

    home_url = "https://swapi.dev/"
    relative_url = "/api/people/{0}"  # magic string
    print(__name__)
    print("current module getting executed")

    print("[INFO] Producing 5 random characters...")
    random_chars = []
    for i in ProduceChars(1, 82):
        random_chars.append(i)
    print(f"[INFO] done - producing random 5 characters")

    output = {}

    for char in random_chars:
        abs_url = home_url + relative_url.format(char)
        print(f"fetching details from - {abs_url}  =>\n")
        response = requests.get(abs_url)
        if response.status_code != 200:
            continue
        else:
            response = response.json()
            response.update({"char_id": char})
            char_data = Characters(**response)
            output.update({char: char_data.name})
            valid_data = remove_cross_reference(char_data)
            table_name = "characters"

            # columns = ["name", "mass", "height", "birth_year",
            #            "hair_color", "skin_color", "eye_color",
            #            "gender", "homeworld"]
            #
            # values = [char_data.name, char_data.mass, char_data.height, char_data.birth_year,
            #           char_data.hair_color, char_data.skin_color, char_data.eye_color,
            #           char_data.gender, char_data.homeworld]
            # primary_key = "char_id"
            #
            # primary_value = char

            insert_resource(table_name, valid_data)

    return jsonify(output)


@swapi.route("/tasktwo")
def task_two():
    """
    This app fetches data of film1 and prints names of characters, vehicles, starships, species and
    planets names.
    """
    film1_url = "https://swapi.dev/api/films/1"
    response = requests.get(film1_url)
    print(f"Fetching details from => {film1_url}\n")
    response = response.json()
    chars = response.get("characters")
    planets = response.get("planets")
    vehicles = response.get("vehicles")
    starships = response.get("starships")
    species = response.get("species")

    def fetch_name(url:str) -> str:
        """
        Hits given url and converts to json data. Extracts only name value from it.
        Returns name.
        :param url: resource url
        :return: name of resource
        """
        print(f"Fetching details from => {url}\n")
        res = requests.get(url)
        if res.status_code != 200:
            return "Not found"
        else:
            res = res.json()
        return res.get("name")

    def get_names(resource:List[str])-> List[str]:
        """
        Returns name from each resource url for given list of urls.
        :param resource: list or resource urls
        :return: list of names
        """
        pool = ThreadPool(15)
        names = pool.map(fetch_name, resource)
        return names

    char_names = get_names(chars)
    planet_names = get_names(planets)
    vehicle_names = get_names(vehicles)
    starship_names = get_names(starships)
    species_names = get_names(species)

    output = {"characters": char_names,
              "planets": planet_names,
              "vehicles": vehicle_names,
              "starships": starship_names,
              "species": species_names}

    return Response(json.dumps(output), status=200, mimetype="application/json")



def remove_cross_reference(data_set: "pydantic datamodel object") -> Dict:
    """
    1. Takes pydantic datamodel object as argument of any resource.
    2. Converts it to dictionary data type.
    3. Removes cross-reference fields if any. (ex., character["url1","url2"])
    4. Converts datetime object to string date in format - "YYYY-MM-DD"
    5. If any field contain None value, converts it into Null, so that it can be inserted into the database.
    6. Returns this formatted dictionary.

    :param data_set: validated pydantic data model object
    :return: Dictionary
    """
    data_set = dict(data_set)
    new_data = data_set.copy()
    for key, value in data_set.items():
        if isinstance(value, list):     # removing cross-reference fields from data object
            new_data.pop(key)
        elif value is None:  # replace None with Null
            new_data[key] = 'Null'

    return new_data


def fetch_url_data(url_list: List[str]) -> List[Dict]:
    """
    1. Hits each url in url list.
    2. Uses ThreadPool to hit urls concurrently and fetches data for each url using map function.
    3. Returns list of dictionary (endpoints data) of each url/api endpoint
    :param url_list: list containing api endpoints
    :return: list of respective endpoint data in json/dict format
    """
    # fetching data for each resource endpoint from film_1
    pool = ThreadPool(25)
    url_data = pool.map(fetch_data, url_list)  # Return data for all urls.
    # map() function returns list
    return url_data


def validate_data(resource: List[Dict], validator: "pydantic datamodel", primary_key) -> List[Dict]:
    """
    For each data in 'resource'-
    1. Does data validation using pydantic datamodel - 'validator'
    2. Removes all fields containing cross-reference urls
    3. appends to new list
    Returns list of dictionary(validated data)

    :param resource: Dictionary of resource data fetched from swapi in json format
    :param validator: pydantic datamodel for data validation
    :return: List of validated data in the Dictionary format
    """
    new_data = []
    for data in resource:
        # breakpoint()
        url = data.get("url")
        url = url.split("/")
        primary_value = [i for i in url if isinstance(i, int)]
        data.update({primary_key: primary_value})
        data = validator(**data)    # validates each url data using pydantic datamodels
        new = remove_cross_reference(data)  # removes cross-reference fields from each url data
        new_data.append(new)
    return new_data


@swapi.route("/taskfour")
def task_four():
    # pull data for the movie "A New Hope"
    film_data = requests.get("https://swapi.dev/api/films/1")
    film_data = film_data.json()
    film_data.update({"film_id": 1})
    film_data = Films(**film_data)

    # fetching urls of each resource in film_1
    charlist = film_data.characters
    planetlist = film_data.planets
    specieslist = film_data.species
    starshipslist = film_data.starships
    vehiclelist = film_data.vehicles

    # Replace the data for each of the endpoint listed in the JSON object.
    char_data = fetch_url_data(charlist)
    planet_data = fetch_url_data(planetlist)
    species_data = fetch_url_data(specieslist)
    starships_data = fetch_url_data(starshipslist)
    vehicle_data = fetch_url_data(vehiclelist)

    # remove all cross-referencing URLs from each resource and validate data using datamodels
    char_data = validate_data(char_data, Characters, "char_id")
    planet_data = validate_data(planet_data, Planets, "planet_id")
    species_data = validate_data(species_data, Species, "species_id")
    starships_data = validate_data(starships_data, Starships, "starship_id")
    vehicle_data = validate_data(vehicle_data, Vehicles, "vehicle_id")

    #  and insert that data into respective database tables
    char_table = "characters"
    for data in char_data:
        print(f"rows affected - {insert_resource(char_table, data)}")

    planet_table = "planet"
    for data in planet_data:
        print(f"rows affected - {insert_resource(planet_table, data)}")

    vehicle_table = "vehicle"
    for data in vehicle_data:
        print(f"rows affected - {insert_resource(vehicle_table, data)}")

    starship_table = "starship"
    for data in starships_data:
        print(f"rows affected - {insert_resource(starship_table, data)}")

    species_table = "species"
    # breakpoint()
    for data in species_data:
        print(f"rows affected - {insert_resource(species_table, data)}")

    film_table = "film"
    film_data = remove_cross_reference(film_data)
    # breakpoint()
    print(f"rows affected - {insert_resource(film_table, film_data)}")

    return jsonify({"Success": 200})