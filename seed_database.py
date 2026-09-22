from app import app
from database import db
from database_models import PlanetDB


planets = [

    PlanetDB(
        name="Mercury",
        mass=3.3011e23,
        gravity=3.70,
        distance_from_sun=57.9,
        moons=0,
        description="Mercury is the closest planet to the Sun."
    ),

    PlanetDB(
        name="Venus",
        mass=4.8675e24,
        gravity=8.87,
        distance_from_sun=108.2,
        moons=0,
        description="Venus is the second planet from the Sun."
    ),

    PlanetDB(
        name="Earth",
        mass=5.972e24,
        gravity=9.81,
        distance_from_sun=149.6,
        moons=1,
        description="Earth is our home planet."
    ),

    PlanetDB(
        name="Mars",
        mass=6.4171e23,
        gravity=3.71,
        distance_from_sun=227.9,
        moons=2,
        description="Mars is known as the Red Planet."
    ),

    PlanetDB(
        name="Jupiter",
        mass=1.898e27,
        gravity=24.79,
        distance_from_sun=778.5,
        moons=95,
        description="Jupiter is the largest planet in the Solar System."
    ),

    PlanetDB(
        name="Saturn",
        mass=5.683e26,
        gravity=10.44,
        distance_from_sun=1434,
        moons=146,
        description="Saturn is famous for its spectacular ring system."
    ),

    PlanetDB(
        name="Uranus",
        mass=8.681e25,
        gravity=8.69,
        distance_from_sun=2871,
        moons=28,
        description="Uranus is an ice giant with a highly tilted axis."
    ),

    PlanetDB(
        name="Neptune",
        mass=1.024e26,
        gravity=11.15,
        distance_from_sun=4495,
        moons=16,
        description="Neptune is the farthest known major planet from the Sun."
    )

]


with app.app_context():

    for planet in planets:

        existing_planet = PlanetDB.query.filter_by(
            name=planet.name
        ).first()

        if existing_planet is None:

            db.session.add(planet)


    db.session.commit()


    print("Solar System database created successfully!")