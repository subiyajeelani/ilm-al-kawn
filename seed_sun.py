from app import app

from database import db

from database_models import SunDB


with app.app_context():

    # Make sure all database tables exist
    db.create_all()

    print("Database tables checked.")


    existing_sun = SunDB.query.first()


    if existing_sun is None:

        sun = SunDB(

            name="Sun",

            mass=1.989e30,

            radius=696340,

            temperature=5778,

            age=4.6,

            description=(
                "The Sun is the star at the center "
                "of our Solar System. Its gravity "
                "keeps the planets in orbit."
            )

        )


        db.session.add(sun)

        db.session.commit()


        print(
            "Sun added successfully!"
        )

    else:

        print(
            "Sun already exists."
        )