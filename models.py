from abc import ABC, abstractmethod
class CelestialBody(ABC):
    """
    Base class for every object in the universe.
    """

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    @abstractmethod
    def describe(self):
     pass

class Planet(CelestialBody):
    """
    Represents a planet.
    """

    def __init__(
        self,
        name,
        mass,
        gravity,
        distance_from_sun,
        moons
    ):
        super().__init__(name, mass)

        self.__gravity = gravity
        self.distance_from_sun = distance_from_sun
        self.moons = moons

    @property
    def gravity(self):
      return self.__gravity

    @gravity.setter
    def gravity(self, value):
      if value <= 0:
        raise ValueError("Gravity must be greater than 0.")

      self.__gravity = value

    def calculate_weight(self, earth_weight):
        """
        Calculate a person's weight on this planet.
        """

        earth_gravity = 9.81

        return earth_weight * (self.gravity / earth_gravity)

    def calculate_orbital_speed(self, central_mass):
     G = 6.67430e-11

     distance_meters = (
       self.distance_from_sun * 1_000_000 * 1000
    )

     return (G * central_mass / distance_meters) ** 0.5

    def calculate_escape_velocity(self, central_mass):
     G = 6.67430e-11
     distance_meters = (
        self.distance_from_sun * 1_000_000 * 1000
    )
     return (2 * G * central_mass / distance_meters) ** 0.5

    def describe(self):
        return (
            f"{self.name} is a planet with "
            f"gravity of {self.gravity} m/s²."
        )

    @property
    def gravity_ratio(self):

        earth_gravity = 9.81

        return self.gravity / earth_gravity


class Moon(CelestialBody):
    """
    Represents a moon.
    """

    def __init__(
        self,
        name,
        mass,
        gravity,
        planet
    ):
        super().__init__(name, mass)

        self.gravity = gravity
        self.planet = planet

    def describe(self):
        return (
            f"{self.name} is a natural satellite "
            f"of {self.planet}."
        )

mercury = Planet(
    "Mercury",
    3.3011e23,
    3.7,
    57.9,
    0
)

venus = Planet(
    "Venus",
    4.8675e24,
    8.87,
    108.2,
    0
)

earth = Planet(
    "Earth",
    5.972e24,
    9.81,
    149.6,
    1
)

mars = Planet(
    "Mars",
    6.4171e23,
    3.71,
    227.9,
    2
)

jupiter = Planet(
    "Jupiter",
    1.898e27,
    24.79,
    778.5,
    95
)

saturn = Planet(
    "Saturn",
    5.683e26,
    10.44,
    1434,
    146
)

uranus = Planet(
    "Uranus",
    8.681e25,
    8.69,
    2871,
    28
)

neptune = Planet(
    "Neptune",
    1.024e26,
    11.15,
    4495,
    16
)

planets = [ 

    mercury,
    venus,
    earth,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune
]

moon = Moon(
    "Moon",
    7.342e22,
    1.62,
    "Earth"
)

# Polymorphism - Common Parent Reference Test

planet_test = Planet(
    "Earth",
    5.972e24,
    9.81,
    149.6e6,
    1
)

moon_test = Moon(
    "Moon",
    7.342e22,
    1.62,
    "Earth"
)

celestial_objects = [
    planet_test,
    moon_test
]

for object in celestial_objects:
    print(object.describe())

