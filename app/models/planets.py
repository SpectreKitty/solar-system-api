class Planet:
    def __init__(self, id, name, description, orbit):
        self.id = id
        self.name = name
        self.description = description
        self.orbit = orbit

planets = [
    Planet(1, "Mercury", "The speedy hotshot!", "first"),
    Planet(2, "Venus", "Beautiful but deadly!", "second"),
    Planet(3, "Earth", "The blue planet!", "third"),
    Planet(4, "Mars", "Potential future home!", "fourth"),
    Planet(5, "Jupiter", "Stormy", "fifth"),
    Planet(6, "Saturn", "Popular, lots of rings", "sixth"),
    Planet(7, "Uranus", "Sideways Spinner", "seventh"),
    Planet(8, "Neptune", "Ice giant", "eighth")
] 