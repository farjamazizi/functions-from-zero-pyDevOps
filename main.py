# from fastapi import FastAPI
# from pydantic import BaseModel
# import uvicorn
# from mylib.logistics import find_coordinate, distanse, total_distanse


# app = FastAPI()


# class City(BaseModel):
#     name: str


# @app.get("/")
# async def root():
#     """List cities with GET HTTP Method

#     Return back a list of cities that are available to get further information about
#     """

#     return {"message": "Hello logistics"}


# if __name__ == "__main__":
#     uvicorn.run(app, port=8080, host="0.0.0.0")
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from mylib.logistics import find_coordinate, distanse, total_distanse


app = FastAPI()


class City(BaseModel):
    name: str


class Route(BaseModel):
    city1: str
    city2: str


class CityRoute(BaseModel):
    cities: list[str]


def _raise_not_found(error: ValueError) -> None:
    raise HTTPException(status_code=404, detail=str(error)) from error


@app.get("/")
async def root():
    """Return a simple service description."""

    return {
        "message": "Hello logistics",
        "endpoints": [
            "/coordinate",
            "/distance",
            "/total-distance",
        ],
    }


@app.post("/coordinate")
async def coordinate(city: City):
    """Return the coordinates for a city."""

    try:
        latitude, longitude = find_coordinate(city.name)
    except ValueError as error:
        _raise_not_found(error)

    return {
        "city": city.name,
        "latitude": latitude,
        "longitude": longitude,
    }


@app.post("/distance")
async def distance(route: Route):
    """Return the distance between two cities."""

    try:
        miles = distanse(route.city1, route.city2)
    except ValueError as error:
        _raise_not_found(error)

    return {
        "from": route.city1,
        "to": route.city2,
        "distance_miles": round(miles, 2),
    }


@app.post("/total-distance")
async def total_distance(route: CityRoute):
    """Return the total distance across an ordered list of cities."""

    try:
        miles = total_distanse(route.cities)
    except ValueError as error:
        _raise_not_found(error)

    return {
        "cities": route.cities,
        "distance_miles": round(miles, 2),
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
