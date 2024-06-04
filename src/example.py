"""
Módulo example.py

Este módulo contiene la funcion get_coordinates que se encarga de obtener las coordenadas de una ciudad a partir de una consulta.
"""

import requests


def get_coordinates(query):
    """
    Este módulo se encarga de obtener las coordenadas de una ciudad a partir de una consulta.

    Args:
        query (str): Ciudad a buscar.

    Returns:
        tuple: Tupla con las coordenadas de la ciudad.
    """
    api_url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
    headers = {"User-Agent": "Testing App"}
    response = requests.get(api_url, headers=headers)

    response_data = response.json()

    return float(response_data[0]["lat"]), float(response_data[0]["lon"])
