"""
(plural API endpoints)
http://127.0.0.1:5000/swapi/people
http://127.0.0.1:5000/swapi/films
http://127.0.0.1:5000/swapi/species
http://127.0.0.1:5000/swapi/vehicles
http://127.0.0.1:5000/swapi/starships
http://127.0.0.1:5000/swapi/planets

(singular API endpoints)
http://127.0.0.1:5000/swapi/people/1
http://127.0.0.1:5000/swapi/films/2
http://127.0.0.1:5000/swapi/species/3
http://127.0.0.1:5000/swapi/vehicles/4
http://127.0.0.1:5000/swapi/starships/5
http://127.0.0.1:5000/swapi/planets/6
"""
from pydantic import parse_obj_as
from typing import List
from flask import Blueprint, Response, jsonify, json
from models.dal.dml import fetch_resources, fetch_resource
from models.datamodels.characters import ResponseCharacters
from models.datamodels.films import ResponseFilms
from models.datamodels.vehicles import ResponseVehicles
from models.datamodels.species import ResponseSpecies
from models.datamodels.planets import ResponsePlanets
from models.datamodels.starships import ResponseStarships


get_data = Blueprint("CRUD", __name__, url_prefix="/swapi")


@get_data.route("/people", methods=["GET"])
def get_characters():
    data = fetch_resources("characters")
    characters = parse_obj_as(List[ResponseCharacters], data)
    response_obj = json.dumps([char.dict() for char in characters])
    # breakpoint()
    return Response(response_obj, status=200, mimetype="application/json")
    # return jsonify(response_obj)


@get_data.route("/vehicles", methods=["GET"])
def get_vehicles():
    data = fetch_resources("vehicle")
    vehicles = parse_obj_as(List[ResponseVehicles], data)
    response_obj = json.dumps([vehicle.dict() for vehicle in vehicles])
    # breakpoint()
    # return jsonify(response_obj) - this doesn't show data in pretty format on postman
    return Response(response_obj, status=200, mimetype="application/json")


@get_data.route("/species", methods=["GET"])
def get_species():
    data = fetch_resources("species")
    species = parse_obj_as(List[ResponseSpecies], data)
    response_obj = json.dumps([spec.dict() for spec in species])
    # breakpoint()
    return Response(response_obj, status=200, mimetype="application/json")


@get_data.route("/starships", methods=["GET"])
def get_starships():
    data = fetch_resources("starship")
    starships = parse_obj_as(List[ResponseStarships], data)
    response_obj = json.dumps([starship.dict() for starship in starships])
    # breakpoint()
    return Response(response_obj, status=200, mimetype="application/json")


@get_data.route("/planets", methods=["GET"])
def get_planets():
    data = fetch_resources("planet")
    planets = parse_obj_as(List[ResponsePlanets], data)
    response_obj = json.dumps([planet.dict() for planet in planets])
    # breakpoint()
    return Response(response_obj, status=200, mimetype="application/json")


@get_data.route("/films", methods=["GET"])
def get_films():
    data = fetch_resources("film")
    films = parse_obj_as(List[ResponseFilms], data)
    response_obj = json.dumps([film.dict() for film in films])
    # breakpoint()
    return Response(response_obj, status=200, mimetype="application/json")


# Singular film url
@get_data.route("/films/<int:index>")
def get_film(index):
    data = fetch_resource("film", "film_id", index)
    # breakpoint()
    if data:
        film = ResponseFilms(**data)
        response_obj = json.dumps(film.dict())
        return Response(response_obj, status=200, mimetype="application/json")
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@get_data.route("/people/<int:index>")
def get_char(index):
    data = fetch_resource("characters", "char_id", index)
    # breakpoint()
    if data:
        peopl = ResponseCharacters(**data)
        response_obj = json.dumps(peopl.dict())
        return Response(response_obj, status=200, mimetype="application/json")
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@get_data.route("/planets/<int:index>")
def get_planet(index):
    data = fetch_resource("planet", "planet_id", index)
    # breakpoint()
    if data:
        planet = ResponsePlanets(**data)
        response_obj = json.dumps(planet.dict())
        return Response(response_obj, status=200, mimetype="application/json")
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@get_data.route("/species/<int:index>")
def get_specie(index):
    data = fetch_resource("species", "species_id", index)
    # breakpoint()
    if data:
        specie = ResponseSpecies(**data)
        response_obj = json.dumps(specie.dict())
        return Response(response_obj, status=200, mimetype="application/json")
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@get_data.route("/vehicles/<int:index>")
def get_vehicle(index):
    data = fetch_resource("vehicle", "vehicle_id", index)
    # breakpoint()
    if data:
        vehicle = ResponseVehicles(**data)
        response_obj = json.dumps(vehicle.dict())
        return Response(response_obj, status=200, mimetype="application/json")
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")


@get_data.route("/starships/<int:index>")
def get_starship(index):
    data = fetch_resource("starship", "starship_id", index)
    # breakpoint()
    if data:
        starship = ResponseStarships(**data)
        response_obj = json.dumps(starship.dict())
        return Response(response_obj, status=200, mimetype="application/json")
    else:
        resp = {"Error": f"No records found for ID - {index}"}
        return Response(json.dumps(resp), status=404, mimetype="application/json")