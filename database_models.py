from database import db


class PlanetDB(db.Model):

    __tablename__ = "planets"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    mass = db.Column(
        db.Float,
        nullable=False
    )

    gravity = db.Column(
        db.Float,
        nullable=False
    )

    distance_from_sun = db.Column(
        db.Float,
        nullable=False
    )

    moons = db.Column(
        db.Integer,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "gravity": self.gravity,
            "distance_from_sun": self.distance_from_sun,
            "moons": self.moons,
            "description": self.description
        }

class SunDB(db.Model):

    __tablename__ = "sun"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(50),
        nullable=False
    )

    mass = db.Column(
        db.Float,
        nullable=False
    )

    radius = db.Column(
        db.Float,
        nullable=False
    )

    temperature = db.Column(
        db.Float,
        nullable=False
    )

    age = db.Column(
        db.Float,
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=False
    )


    def to_dict(self):

        return {

            "id": self.id,

            "name": self.name,

            "mass": self.mass,

            "radius": self.radius,

            "temperature": self.temperature,

            "age": self.age,

            "description": self.description

        }

class MoonDB(db.Model): 

    __tablename__= "moons"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(50),
        nullable=False
    )

    mass = db.Column(
        db.Float,
        nullable=False
    )

    radius = db.Column(
        db.Float,
        nullable=False
    )

    gravity = db.Column(
        db.Float,
        nullable=False
    )

    orbital_period = db.Column(
        db.Float,
        nullable=False
    )

    planet_id = db.Column(
        db.Integer,
        db.ForeignKey("planets.id"),
        nullable=False
    )

    planet = db.relationship(
        "PlanetDB",
        backref="moons_data"
    )

    description = db.Column(
        db.Text,
        nullable=False
    )

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "mass": self.mass,
            "radius": self.radius,
            "gravity": self.gravity,
            "orbital_period": self.orbital_period,

            "planet": {
                "id": self.planet.id,
                "name": self.planet.name,
                "gravity": self.planet.gravity
            },

            "description": self.description
        }