from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.planets import Planet


planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()

    try:
        new_planet = Planet.from_dict(request_body)

        db.session.add(new_planet)
        db.session.commit()

        response_body = new_planet.to_dict()
        # response_body.to_dict = {
        #     "id": new_planet.id,
        #     "name": new_planet.name,
        #     "description": new_planet.description,
        #     "orbit": new_planet.orbit
        #     }
        return response_body, 201
    
    except KeyError as e:
        response = {"message": f"Invalid request: missing {e.args[0]}"}
        abort(make_response(response, 400))

@planets_bp.get("")
def get_all_planets():
    # query = db.select(Planet).order_by(Planet.id)
    # planets = db.session.scalars(query)
    query = db.select(Planet)
    
    name_param = request.args.get("name")
    if name_param:
        query = db.select(Planet).where(Planet.name == name_param)

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))

    orbit_param = request.args.get("orbit")
    if orbit_param:
        query = query.where(Planet.orbit.ilike(f"%{orbit_param}%"))

    planets = db.session.scalars(query.order_by(Planet.id))
    
    response_list = []

    for planet in planets:
        response_list.append(planet.to_dict())
    return response_list

@planets_bp.get("<planet_id>")
def get_one_planet(planet_id):
    planet = validate_model(Planet, planet_id)

    return planet.to_dict()

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        response = {"message": f"{cls.__name__} {model_id} is invalid"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"message": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404))
    
    return model

@planets_bp.put("/<planet_id>")
def update_planet(model_id):
    planet = validate_model(Planet, model_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.orbit = request_body["orbit"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planets_bp.delete("/<planet_id>")
def delete_planet(model_id):
    planet = validate_model(Planet, model_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


    

