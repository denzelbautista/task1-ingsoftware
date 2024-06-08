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


@app.route("/geoapi/distance/<lat1_lon1>/<lat2_lon2>", methods=["GET"])
def get_distance(lat1_lon1, lat2_lon2):
    """
    Este endpoint se encarga de obtener la distancia entre dos puntos geográficos
    utilizando la libreria geopy para facilitar el cálculo.

    Endpoint:
        /geoapi/distance/{lat1_lon1}/{lat2_lon2}
        
    Args:
        lat1_lon1 (str): Coordenadas del primer punto en formato "latitud, longitud".
        lat2_lon2 (str): Coordenadas del segundo punto en formato "latitud, longitud".

    Returns:
        json: json con la distancia en la clave "distance" y las unidades en la clave "units".
    """
    # Separa las coordenadas en latitud y longitud
    lat1, lon1 = lat1_lon1.split(',')
    lat2, lon2 = lat2_lon2.split(',')

    # Convierte las coordenadas a flotantes
    lat1, lon1 = float(lat1), float(lon1)
    lat2, lon2 = float(lat2), float(lon2)

    # Calcula la distancia usando geopy
    distance = geodesic((lat1, lon1), (lat2, lon2)).kilometers

    # Devuelve la distancia calculada
    return make_response(jsonify({"distance": distance, "units": "kilometers"}),200)


if __name__ == "__main__":
    app.run()
