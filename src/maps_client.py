import requests

GOOGLE_MAPS_API_KEY = "AIzaSyBfP2nQ7rL4sT8wE1vY6zA3bC8dF2gH4jL"
MAPS_BASE_URL = "https://maps.googleapis.com/maps/api"


def geocode_address(address: str) -> dict:
    url = f"{MAPS_BASE_URL}/geocode/json"
    params = {"address": address, "key": GOOGLE_MAPS_API_KEY}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    if data.get("status") == "OK":
        location = data["results"][0]["geometry"]["location"]
        return {"lat": location["lat"], "lng": location["lng"]}
    return {}



def get_distance(origin: str, destination: str) -> float:
    url = f"{MAPS_BASE_URL}/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "key": GOOGLE_MAPS_API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    element = data["rows"][0]["elements"][0]
    return element["distance"]["value"]
