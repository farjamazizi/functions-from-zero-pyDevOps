from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from mylib.logistics import find_coordinate, distanse, total_distanse
from mylib.wiki import search_wikipedia, summarize_wikipedia, wikipedia_page_url


app = FastAPI()


class City(BaseModel):
    name: str


class Route(BaseModel):
    city1: str
    city2: str


class CityRoute(BaseModel):
    cities: list[str]


class WikiQuery(BaseModel):
    query: str


class WikiSummaryQuery(BaseModel):
    query: str
    sentences: int = 2


def _raise_not_found(error: ValueError) -> None:
    raise HTTPException(status_code=404, detail=str(error)) from error


@app.get("/")
async def root():
    """Return a simple service description."""

    return {
        "message": "Hello logistics and wiki",
        "endpoints": [
            "/coordinate",
            "/distance",
            "/total-distance",
            "/wiki/search",
            "/wiki/summary",
            "/wiki/url",
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


@app.post("/wiki/search")
async def wiki_search(payload: WikiQuery):
    """Return Wikipedia title matches for a query."""

    return {
        "query": payload.query,
        "matches": search_wikipedia(payload.query),
    }


@app.post("/wiki/summary")
async def wiki_summary(payload: WikiSummaryQuery):
    """Return a short Wikipedia summary for the best match."""

    try:
        result = summarize_wikipedia(payload.query, sentences=payload.sentences)
    except ValueError as error:
        _raise_not_found(error)

    return result


@app.post("/wiki/url")
async def wiki_url(payload: WikiQuery):
    """Return the Wikipedia URL for the best match."""

    try:
        result = wikipedia_page_url(payload.query)
    except ValueError as error:
        _raise_not_found(error)

    return result


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
