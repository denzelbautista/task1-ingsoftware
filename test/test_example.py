"""
Módulo de pruebas para example.py

Este módulo contiene pruebas unitarias para verificar el funcionamiento de las funciones en example.py.
"""

import pytest
import src.example as example


def test_can_call_existing_endpoints_of_the_API():
    """
    Test para probar si se puede llamar a los endpoints existentes de la API.

    Args:
        None

    Returns:
        None
    """
    try:
        detected = example.get_coordinates("Lima,Perú")
    except:
        assert False, "Exception while calling an existing function"


def test_cannot_call_nonexisting_endpoints_of_the_API():
    """
    Test para probar si no se puede llamar a los endpoints no existentes de la API.

    Args:
        None

    Returns:
        None
    """
    try:
        detected = example.something_not_existent("Lima,Perú")
        assert False, "I was able to call a non-existent function"
    except:
        pass


def test_endpoint_returns_something():
    """
    Test para probar si el endpoint retorna algo.

    Args:
        None

    Returns:
        None

    """
    try:
        detected = example.get_coordinates("Lima,Perú")
        assert detected is not None
    except:
        assert False, "Exception while calling an existing function"


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

    return abs(point1[0] - point2[0]) < 0.1 and abs(point1[1] - point2[1]) < 0.1


def test_the_result_is_correct_for_lima():
    """
    Test para verificar si las coordenadas obtenidas para Lima, Perú son correctas.

    Args:
        None
    Returns:
        None
    """
    # lima coordinates
    expected = -12.0463731, -77.042754
    detected = example.get_coordinates("Lima,Perú")
    assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_buenos_aires():
    """
    Test para verificar si las coordenadas obtenidas para Lima, Perú son correctas.

    Args:
        None
    Returns:
        None
    """
    # buenos aires coordinates
    expected = -34.6075682, -58.4370894
    detected = example.get_coordinates("Buenos Aires, Argentina")
    assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_quito():
    """
    Test para verificar si las coordenadas obtenidas para Lima, Perú son correctas.

    Args:
        None
    Returns:
        None
    """
    # quito coordinates
    expected = -0.2201641, -78.5123274
    detected = example.get_coordinates("Quito, Ecuador")
    assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_bogota():
    """
    Test para verificar si las coordenadas obtenidas para Lima, Perú son correctas.

    Args:
        None
    Returns:
        None

    """
    # bogota coordinates
    expected = 4.598077, -74.076102
    detected = example.get_coordinates("Bogotá, Colombia")
    assert near(detected, expected), "The result is not the expected one"
