"""
Módulo de pruebas para geoapi.py

Este módulo contiene pruebas unitarias para verificar el funcionamiento de las funciones en geoapi.py.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.geoapi import app
def test_can_call_existing_endpoints_of_the_API():
    """
    Test para probar si se puede llamar a los endpoints existentes de la API.

    Args:
        None

    Returns:
        None
    """
    with app.test_client() as client:
        response = client.get('/geoapi/coordinates/Lima,Perú')
        assert response.status_code == 200


def test_cannot_call_nonexisting_endpoints_of_the_API():
    """
    Test para probar si no se puede llamar a los endpoints no existentes de la API.

    Args:
        None

    Returns:
        None
    """
    with app.test_client() as client:
        response = client.get('/geoapi/non_existent_endpoint')
        assert response.status_code == 404


def test_endpoint_returns_something():
    """
    Test para probar si el endpoint retorna algo.

    Args:
        None

    Returns:
        None
    """
    with app.test_client() as client:
        response = client.get('/geoapi/coordinates/Lima,Perú')
        assert response.json is not None


def near(point1, point2):
    """
    Función para verificar si dos puntos son cercanos, esta tiene un margen de error de 0.1, lo que significa
    que si la diferencia entre los puntos es menor a 0.1, se consideran iguales.

    Args:
        point1 (tuple): Primer punto a comparar.
        point2 (tuple): Segundo punto a comparar.

    Returns:
        bool: True si los puntos son cercanos, False en caso contrario.

    """
    return abs(float(point1[0]) - float(point2[0])) < 0.1 and abs(float(point1[1]) - float(point2[1])) < 0.1


def test_the_result_is_correct_for_lima():
    """
    Test para verificar si las coordenadas obtenidas para Lima, Perú son correctas.

    Args:
        None
    Returns:
        None
    """
    with app.test_client() as client:
        expected = (-12.0463731, -77.042754)
        response = client.get('/geoapi/coordinates/Lima,Perú')
        detected = (response.json["lat"], response.json["lon"])
        assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_buenos_aires():
    """
    Test para verificar si las coordenadas obtenidas para Buenos Aires, Argentina son correctas.

    Args:
        None
    Returns:
        None
    """
    with app.test_client() as client:
        expected = (-34.6075682, -58.4370894)
        response = client.get('/geoapi/coordinates/Buenos Aires, Argentina')
        detected = (response.json["lat"], response.json["lon"])
        assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_quito():
    """
    Test para verificar si las coordenadas obtenidas para Quito, Ecuador son correctas.

    Args:
        None
    Returns:
        None
    """
    with app.test_client() as client:
        expected = (-0.2201641, -78.5123274)
        response = client.get('/geoapi/coordinates/Quito, Ecuador')
        detected = (response.json["lat"], response.json["lon"])
        assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_bogota():
    """
    Test para verificar si las coordenadas obtenidas para Bogotá, Colombia son correctas.

    Args:
        None
    Returns:
        None
    """
    with app.test_client() as client:
        expected = (4.598077, -74.076102)
        response = client.get('/geoapi/coordinates/Bogotá, Colombia')
        detected = (response.json["lat"], response.json["lon"])
        assert near(detected, expected), "The result is not the expected one"

def test_invalid_city_name():
    """
    Test para verificar si se maneja correctamente un nombre de ciudad no válido.

    Args:
        None

    Returns:
        None
    """
    with app.test_client() as client:
        city_name = "Invalid City Name"
        response = client.get(f'/geoapi/coordinates/{city_name}')
        assert response.status_code == 400
        assert response.json['success'] == False

def test_can_call_distance_endpoint():
    """
    Test para probar si se puede llamar al endpoint de distancia de la API.

    Args:
        None

    Returns:
        None
    """
    with app.test_client() as client:
        response = client.get('/geoapi/distance/-12.0463731,-77.042754/-34.6075682,-58.4370894')
        assert response.status_code == 200


def test_distance_endpoint_returns_something():
    """
    Test para probar si el endpoint de distancia retorna algo.

    Args:
        None

    Returns:
        None
    """
    with app.test_client() as client:
        response = client.get('/geoapi/distance/-12.0463731,-77.042754/-34.6075682,-58.4370894')
        assert response.json is not None


def distance_near(detected_distance, expected_distance, tolerance=50):
    """
    Función para verificar si la distancia detectada está dentro de un margen de error con respecto a la distancia esperada.

    Args:
        detected_distance (float): La distancia calculada entre dos puntos.
        expected_distance (float): La distancia esperada entre los dos puntos.
        tolerance (float): El margen de error permitido. Default es 50 km.

    Returns:
        bool: True si la distancia detectada está dentro del margen de error, False en caso contrario.
    """
    return abs(detected_distance - expected_distance) < tolerance


def test_the_distance_is_correct():
    """
    Test para verificar si la distancia obtenida entre Lima, Perú y Buenos Aires, Argentina es correcta.

    Args:
        None
    Returns:
        None
    """
    with app.test_client() as client:
        response = client.get('/geoapi/distance/-12.0463731,-77.042754/-34.6075682,-58.4370894')
        distance = response.json["distance"]
        expected_distance = 3144.0  # Aproximadamente la distancia en kilómetros entre Lima y Buenos Aires
        assert distance_near(distance, expected_distance), "The distance is not the expected one"
