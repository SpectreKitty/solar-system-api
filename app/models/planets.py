from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
        id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
        name: Mapped[str]
        description: Mapped[str]
        orbit: Mapped[str]

        def to_dict(self):
                planet_as_dict = {}
                planet_as_dict["id"] = self.id
                planet_as_dict["name"] = self.name
                planet_as_dict["description"] = self.description
                planet_as_dict["orbit"] = self.orbit

                return planet_as_dict

        @classmethod
        def from_dict(cls, planet_data):
                return cls(name=planet_data["name"], description=planet_data["description"], orbit=planet_data["orbit"])

# planets = [
#     Planet(1, "Mercury", "The speedy hotshot!", "first"),
#     Planet(2, "Venus", "Beautiful but deadly!", "second"),
#     Planet(3, "Earth", "The blue planet!", "third"),
#     Planet(4, "Mars", "Potential future home!", "fourth"),
#     Planet(5, "Jupiter", "Stormy", "fifth"),
#     Planet(6, "Saturn", "Popular, lots of rings", "sixth"),
#     Planet(7, "Uranus", "Sideways Spinner", "seventh"),
#     Planet(8, "Neptune", "Ice giant", "eighth")
# ] 