"""
http://127.0.0.1:5000/swapi/people
http://127.0.0.1:5000/swapi/films
http://127.0.0.1:5000/swapi/species
http://127.0.0.1:5000/swapi/vehicles
http://127.0.0.1:5000/swapi/starships
http://127.0.0.1:5000/swapi/planets
"""
from typing import Dict
from pydantic import ValidationError
from flask import Blueprint, request, Response, json
from models.datamodels.characters import Characters
from models.datamodels.films import Films
from models.datamodels.vehicles import Vehicles
from models.datamodels.species import Species
from models.datamodels.starships import Starships
from models.datamodels.planets import Planets
from models.dal.dml import insert_resource


post_data = Blueprint("post_data", __name__, url_prefix="/swapi")


def remove_cross_reference(data_set: "pydantic datamodel object") -> Dict:
    """
    1. Takes pydantic datamodel object as argument of any resource.
    2. Converts it to dictionary data type.
    3. Removes cross-reference fields if any. (ex., character["url1","url2"]) or None fields.
    4. Returns this formatted dictionary.

    :param data_set: validated pydantic data model object
    :return: Data in dictionary without cross-reference and None fields.
    """
    data_set = dict(data_set)
    new_data = data_set.copy()
    # breakpoint()
    for key, value in data_set.items():
        if isinstance(value, list) or value is None:
            # removing cross-reference and None fields from data object
            new_data.pop(key)

    return new_data


@post_data.post("/people")
def post_characters():
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("species_id") is None:
        url = request_data.get("url")
        url = url.split("/")
        request_data["species_id"] = url[-2]
    response_obj = {}
    try:
        request_data = Characters(**request_data)
        request_data = remove_cross_reference(request_data)
        result = insert_resource("characters", request_data)
        response_obj = {
            "rows_affected": result,
            "character_name": request_data.get("name"),
            "message": "record created successfully" if result else "Error! record already exists"
        }

    except ValidationError as e:
        # breakpoint()
        error_msg = str(e)
        # breakpoint()
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=200, mimetype="application/json")


@post_data.route("/films", methods=["POST"])
def post_films():
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("species_id") is None:
        url = request_data.get("url")
        url = url.split("/")
        request_data["species_id"] = url[-2]
    response_obj = {}
    try:
        request_data = Films(**request_data)
        request_data = remove_cross_reference(request_data)
        result = insert_resource("film", request_data)
        response_obj = {
            "rows_affected": result,
            "film_name": request_data.get("title"),
            "message": "record created successfully" if result else "Error! record already exists"
        }

    except ValidationError as e:
        # breakpoint()
        error_msg = str(e)
        # breakpoint()
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=201, mimetype="application/json")


@post_data.route("/vehicles", methods=["POST"])
def post_vehicles():
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("species_id") is None:
        url = request_data.get("url")
        url = url.split("/")
        request_data["species_id"] = url[-2]
    response_obj = {}
    try:
        request_data = Vehicles(**request_data)
        request_data = remove_cross_reference(request_data)
        result = insert_resource("vehicle", request_data)
        response_obj = {
            "rows_affected": result,
            "Vehicle_name": request_data.get("name"),
            "message": "record created successfully" if result else "Error! record already exists"
        }

    except ValidationError as e:
        # breakpoint()
        error_msg = str(e)
        # breakpoint()
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=201, mimetype="application/json")


@post_data.route("/starships", methods=["POST"])
def post_starships():
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("species_id") is None:
        url = request_data.get("url")
        url = url.split("/")
        request_data["species_id"] = url[-2]
    response_obj = {}
    try:
        request_data = Starships(**request_data)
        request_data = remove_cross_reference(request_data)
        result = insert_resource("starship", request_data)
        response_obj = {
            "rows_affected": result,
            "starship_name": request_data.get("name"),
            "message": "record created successfully" if result else "Error! record already exists"
        }

    except ValidationError as e:
        # breakpoint()
        error_msg = str(e)
        # breakpoint()
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=201, mimetype="application/json")


@post_data.route("/species", methods=["POST"])
def post_species():
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("species_id") is None:
        url = request_data.get("url")
        url = url.split("/")
        request_data["species_id"] = url[-2]

    # breakpoint()
    response_obj = {}
    try:
        request_data = Species(**request_data)
        request_data = remove_cross_reference(request_data)
        breakpoint()
        result = insert_resource("species", request_data)
        response_obj = {
            "rows_affected": result,
            "species_name": request_data.get("name"),
            "message": "record created successfully" if result else "Error! record already exists"
        }

    except ValidationError as e:
        # breakpoint()
        error_msg = str(e)
        # breakpoint()
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=201, mimetype="application/json")


@post_data.route("/planets", methods=["POST"])
def post_planets():
    # breakpoint()
    request_data = dict(request.args) if request.args else request.json
    if request_data.get("species_id") is None:
        url = request_data.get("url")
        url = url.split("/")
        request_data["species_id"] = url[-2]
    response_obj = {}
    try:
        request_data = Planets(**request_data)
        request_data = remove_cross_reference(request_data)
        result = insert_resource("planet", request_data)
        response_obj = {
            "rows_affected": result,
            "planet_name": request_data.get("name"),
            "message": "record created successfully" if result else "Error! record already exists"
        }

    except ValidationError as e:
        # breakpoint()
        error_msg = str(e)
        # breakpoint()
        response_obj = {"ValidationError": error_msg}

    except Exception as e:
        error_msg = str(e)
        response_obj = {"Error": error_msg}

    finally:
        return Response(json.dumps(response_obj), status=201, mimetype="application/json")
