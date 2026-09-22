console.log("ILM-AL-KAWN JavaScript loaded");


async function loadPlanets() {

    console.log("loadPlanets() started");


    const container =
        document.getElementById("planet-container");


    if (!container) {

        console.error(
            "planet-container not found!"
        );

        return;
    }


    try {

        const response =
            await fetch("/api/planets");


        console.log(
            "API status:",
            response.status
        );


        const planets =
            await response.json();


        console.log(
            "Planets received:",
            planets
        );


        container.innerHTML = "";


        planets.forEach(function (planet) {

            console.log(
                "Creating:",
                planet.name
            );


            const element =
                document.createElement("div");


            element.className =
                "planet dynamic-planet";


            element.innerHTML = `

                <div class="planet-icon">
                    ${getPlanetIcon(planet.name)}
                </div>

                <span>
                    ${planet.name}
                </span>

            `;


            element.onclick = function () {

                showPlanet(planet);

            };


            container.appendChild(element);

        });


        console.log(
            "ALL PLANETS RENDERED"
        );

    }


    catch (error) {

        console.error(
            "ERROR:",
            error
        );

    }

}


function getPlanetIcon(name) {

    const icons = {

        Mercury: "☿",
        Venus: "♀",
        Earth: "🌍",
        Mars: "♂",
        Jupiter: "♃",
        Saturn: "♄",
        Uranus: "♅",
        Neptune: "♆"

    };


    return icons[name] || "🪐";

}


function showPlanet(planet) {

    const info =
        document.getElementById(
            "planet-info"
        );


    info.innerHTML = `

        <h2>${planet.name}</h2>

        <p>
            ${planet.description}
        </p>

        <div class="facts">

            <div class="fact">

                <strong>Gravity</strong>

                <span>
                    ${planet.gravity} m/s²
                </span>

            </div>


            <div class="fact">

                <strong>Distance from Sun</strong>

                <span>
                    ${planet.distance_from_sun}
                    million km
                </span>

            </div>


            <div class="fact">

                <strong>Moons</strong>

                <span>
                    ${planet.moons}
                </span>

            </div>


            <div class="fact">

                <strong>Mass</strong>

                <span>
                    ${Number(planet.mass).toExponential(3)}
                    kg
                </span>

            </div>

        </div>

    `;

}


function scrollToSolarSystem() {

    document
        .getElementById("solar-system")
        .scrollIntoView({
            behavior: "smooth"
        });

}


// START

loadPlanets();