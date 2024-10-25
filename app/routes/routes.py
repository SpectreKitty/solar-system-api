from flask import Blueprint, abort, make_response
from ..db import db
from app.models.planets import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.get("")
def get_all_planets():
    response_list = []

    for planet in planets:
        response_list.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            orbit=planet.orbit
        ))
    
    return response_list

@planets_bp.get("<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return dict(
        id=planet.id,
        name=planet.name,
        description=planet.description,
        orbit=planet.orbit
            )

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        response = {"message": f"Planet {planet_id} is invalid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == planet_id:
            return planet

    response = {"message":f"Planet {planet_id} not found"}
    abort(make_response(response, 404))
