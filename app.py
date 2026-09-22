from flask import Flask, render_template, jsonify, request

from database import db
from database_models import PlanetDB, SunDB, MoonDB
from models import Planet, Moon

app = Flask(__name__)


# --------------------------------
# DATABASE CONFIGURATION
# --------------------------------

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ilm_kawn.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)


# --------------------------------
# HOME
# --------------------------------

@app.route("/")
def home():

    return render_template("index.html")


# --------------------------------
# GET ALL PLANETS
# --------------------------------

@app.route("/api/planets")
def get_planets():

    planets = PlanetDB.query.all()

    result = []

    for planet_data in planets:

        # -----------------------------
        # DATABASE → OOP OBJECT
        # -----------------------------

        planet = Planet(

            planet_data.name,

            planet_data.mass,

            planet_data.gravity,

            planet_data.distance_from_sun,

            planet_data.moons

        )


        # -----------------------------
        # DATABASE INFORMATION
        # + OOP CALCULATION
        # -----------------------------

        planet_info = planet_data.to_dict()

        planet_info["gravity_ratio"] = round(
            planet.gravity_ratio,
            3
        )


        result.append(
            planet_info
        )


    return jsonify(result)


# --------------------------------
# GET ONE PLANET
# --------------------------------

@app.route("/api/planets/<planet_name>")
def get_planet(planet_name):

    planet_data = PlanetDB.query.filter_by(
        name=planet_name
    ).first()

    if not planet_data:
        return jsonify({
            "error": "Planet not found"
        }), 404

    planet = Planet(
        planet_data.name,
        planet_data.mass,
        planet_data.gravity,
        planet_data.distance_from_sun,
        planet_data.moons
    )

    planet_info = planet_data.to_dict()

    planet_info["gravity_ratio"] = round(
        planet.gravity_ratio,
        3
    )

    return jsonify(planet_info)


# --------------------------------
# CALCULATE WEIGHT
# --------------------------------

@app.route(
    "/api/calculate-weight",
    methods=["POST"]
)
def calculate_weight():

    data = request.get_json()

    earth_weight = data.get("weight")
    planet_name = data.get("planet")


    # Check weight

    if earth_weight is None:

        return jsonify({
            "error": "Weight is required."
        }), 400


    # Check planet

    if planet_name is None:

        return jsonify({
            "error": "Planet is required."
        }), 400


    # Convert weight to number

    try:

        earth_weight = float(
            earth_weight
        )

    except (TypeError, ValueError):

        return jsonify({
            "error": "Weight must be a number."
        }), 400


    # Check positive value

    if earth_weight <= 0:

        return jsonify({
            "error": "Weight must be greater than zero."
        }), 400


    # Get planet from database

    planet_data = PlanetDB.query.filter_by(
        name=planet_name
    ).first()


    if planet_data is None:

        return jsonify({
            "error": "Planet not found."
        }), 404


    # --------------------------------
    # DATABASE → OOP OBJECT
    # --------------------------------

    planet = Planet(

        planet_data.name,

        planet_data.mass,

        planet_data.gravity,

        planet_data.distance_from_sun,

        planet_data.moons

    )


    # --------------------------------
    # PYTHON OOP CALCULATION
    # --------------------------------

    planet_weight = planet.calculate_weight(
        earth_weight
    )


    return jsonify({

        "planet": planet.name,

        "earth_weight": earth_weight,

        "planet_weight": round(
            planet_weight,
            2
        )

    })

# --------------------------------
# GET SUN
# --------------------------------

@app.route("/api/sun")
def get_sun():

    sun = SunDB.query.first()

    if sun is None:

        return jsonify({
            "error": "Sun data not found."
        }), 404

    return jsonify(
        sun.to_dict()
    )
# --------------------------------
# GET MOON
# --------------------------------

@app.route("/api/moon")
def get_moon():

    moon = MoonDB.query.first()

    if moon is None:

        return jsonify({
            "error": "Moon data not found."
        }), 404

    return jsonify(
        moon.to_dict()
    )

@app.route("/api/polymorphism")
def polymorphism_demo():

    planet = Planet(
        "Earth",
        5.972e24,
        9.81,
        149.6e6,
        1
    )

    moon = Moon(
        "Moon",
        7.342e22,
        1.62,
        "Earth"
    )

    celestial_objects = [
        planet,
        moon
    ]

    result = []

    for obj in celestial_objects:

        result.append({
            "name": obj.name,
            "class": obj.__class__.__name__,
            "method": "describe()",
            "description": obj.describe()
        })

    return jsonify(result)

# --------------------------------
# COMPARE TWO PLANETS
# --------------------------------

@app.route("/api/compare")
def compare_planets():

    planet1_name = request.args.get(
        "planet1"
    )

    planet2_name = request.args.get(
        "planet2"
    )


    # Check both planets were provided

    if not planet1_name or not planet2_name:

        return jsonify({
            "error":
                "Please provide two planet names."
        }), 400


    # Get first planet

    planet1_data = PlanetDB.query.filter_by(
        name=planet1_name
    ).first()


    # Get second planet

    planet2_data = PlanetDB.query.filter_by(
        name=planet2_name
    ).first()


    # Check first planet

    if planet1_data is None:

        return jsonify({
            "error":
                f"{planet1_name} not found."
        }), 404


    # Check second planet

    if planet2_data is None:

        return jsonify({
            "error":
                f"{planet2_name} not found."
        }), 404


    # --------------------------------
    # DATABASE → OOP OBJECTS
    # --------------------------------

    planet1 = Planet(

        planet1_data.name,

        planet1_data.mass,

        planet1_data.gravity,

        planet1_data.distance_from_sun,

        planet1_data.moons

    )


    planet2 = Planet(

        planet2_data.name,

        planet2_data.mass,

        planet2_data.gravity,

        planet2_data.distance_from_sun,

        planet2_data.moons

    )


    # --------------------------------
    # BUILD COMPARISON
    # --------------------------------

    comparison = {

        "planet1": {

            "name": planet1.name,

            "mass": planet1.mass,

            "gravity": planet1.gravity,

            "distance_from_sun":
                planet1.distance_from_sun,

            "moons": planet1.moons,

            "gravity_ratio":
                round(
                    planet1.gravity_ratio,
                    3
                )

        },

        "planet2": {

            "name": planet2.name,

            "mass": planet2.mass,

            "gravity": planet2.gravity,

            "distance_from_sun":
                planet2.distance_from_sun,

            "moons": planet2.moons,

            "gravity_ratio":
                round(
                    planet2.gravity_ratio,
                    3
                )

        }

    }


    return jsonify(
        comparison
    )

# --------------------------------
# CREATE DATABASE TABLES
# --------------------------------

with app.app_context():

    db.create_all()



@app.route("/api/abstraction")
def abstraction_demo():

    return jsonify({
        "abstract_class": "CelestialBody",
        "abstract_method": "describe()",
        "implementations": [
            {
                "class": "Planet",
                "description": "Planet provides its own describe() implementation."
            },
            {
                "class": "Moon",
                "description": "Moon provides its own describe() implementation."
            }
        ],
        "key_idea": (
            "An abstract class defines what child classes must provide."
        )
    })

@app.route("/api/orbital-speed/<planet_name>")
def get_orbital_speed(planet_name):

    planet_data = PlanetDB.query.filter_by(
        name=planet_name
    ).first()

    if not planet_data:
        return jsonify({
            "error": "Planet not found"
        }), 404

    planet = Planet(
        planet_data.name,
        planet_data.mass,
        planet_data.gravity,
        planet_data.distance_from_sun,
        planet_data.moons
    )

    sun = SunDB.query.first()

    if not sun:
        return jsonify({
            "error": "Sun data not found"
        }), 404

    orbital_speed = planet.calculate_orbital_speed(
        sun.mass
    )

    return jsonify({
        "planet": planet.name,
        "orbital_speed_mps": round(
            orbital_speed,
            2
        ),
        "orbital_speed_kmps": round(
            orbital_speed / 1000,
            2
        )
    })

@app.route("/api/escape-velocity/<planet_name>")
def get_escape_velocity(planet_name):
    planet_data = PlanetDB.query.filter_by(name=planet_name).first()

    if not planet_data:
        return jsonify({"error": "Planet not found"}), 404

    planet = Planet(
        planet_data.name,
        planet_data.mass,
        planet_data.gravity,
        planet_data.distance_from_sun,
        planet_data.moons
    )

    sun = SunDB.query.first()

    if not sun:
        return jsonify({"error": "Sun data not found"}), 404

    escape_velocity = planet.calculate_escape_velocity(sun.mass)

    return jsonify({
        "planet": planet.name,
        "escape_velocity_mps": round(escape_velocity, 2),
        "escape_velocity_kmps": round(escape_velocity / 1000, 2)
    })
# --------------------------------
# RUN APPLICATION
# --------------------------------

if __name__ == "__main__":

    app.run(debug=True)