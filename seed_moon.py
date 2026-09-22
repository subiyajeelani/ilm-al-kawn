from app import app

from database import db

from database_models import MoonDB, PlanetDB


with app.app_context():

    db.create_all()

    earth = PlanetDB.query.filter_by(
        name="Earth"
    ).first()


    if earth is None:

        print(
            "Earth was not found in database."
        )

    else:

        existing_moon = MoonDB.query.filter_by(
            name="Moon"
        ).first()


        if existing_moon is None:

            moon = MoonDB(

                name="Moon",

                mass=7.342e22,

                radius=1737.4,

                gravity=1.62,

                orbital_period=27.3,

                planet_id=earth.id,

                description=(
                    "The Moon is Earth's natural "
                    "satellite and the fifth-largest "
                    "moon in the Solar System."
                )

            )


            db.session.add(moon)

            db.session.commit()


            print(
                "Moon added successfully!"
            )

        else:

            print(
                "Moon already exists."
            )