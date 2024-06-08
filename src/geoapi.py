"""
Módulo geoapi.py

Este módulo contienes las rutas geoapi/coordinates/{cityname} y geoapi/distance/{lat1_lon1}/{lat2_lon2} 
con las funciones get_coordinates y get_distance respectivamente.
"""

from flask import Flask, request, jsonify,make_response
from geopy.distance import geodesic
import requests

app = Flask(__name__)


@app.route("/geoapi/coordinates/<city_country>", methods=["GET"])
def get_coordinates(city_country):
    """
    Este endpoint se encarga de obtener las coordenadas de una ciudad a partir de una consulta
    a la api de openstreetmap.

    Endpoint:
        /geoapi/coordinates/{city_country}

    Args:
        city_country (str): Ciudad a buscar en formato "ciudad, pais" o "pais, ciudad".

    Returns:
        json: json con las coordenadas de la ciudad en las claves "lat" y "lon".
    """
    api_url = f"https://nominatim.openstreetmap.org/search?q={city_country}&format=json"
    headers = {"User-Agent": "Testing App University"}
    response = requests.get(api_url, headers=headers)

    response_data = response.json()

    ciudad_encontrada = None

    for elemento_respuesta in response_data:
        if elemento_respuesta["addresstype"] == 'city':
            ciudad_encontrada = elemento_respuesta
            break

    if ciudad_encontrada:
        lat = ciudad_encontrada["lat"]
        lon = ciudad_encontrada["lon"]

        return make_response(jsonify({"success": True, "lat": lat, "lon": lon}),200)
    else:
        return make_response(jsonify({"success": False, "error" : "It's not a city name or incorrect input"}), 400)



if __name__ == "__main__":
    app.run()
