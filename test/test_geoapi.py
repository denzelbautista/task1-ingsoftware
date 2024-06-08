"""
Módulo de pruebas para geoapi.py

Este módulo contiene pruebas unitarias para verificar el funcionamiento de las funciones en geoapi.py.
"""

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
        assert abs(distance - expected_distance) < 10, "The distance is not the expected one"
