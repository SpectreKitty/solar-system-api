from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.planets import Planet

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    orbit = request_body["orbit"]

    new_planet = Planet(name=name, description=description, orbit=orbit)
    db.session.add(new_planet)
    db.session.commit()

    response_body = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "orbit": new_planet.orbit
    }

    return response_body, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)

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

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"book {planet_id} not found"}
        abort(make_response(response, 404))
    
    return planet

@planets_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.orbit = request_body["orbit"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<planet_id>")
def delete_planet(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


    

