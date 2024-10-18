from flask import Blueprint
from app.models.planets import planets

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