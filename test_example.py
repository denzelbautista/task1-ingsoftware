"""













algo.py
"""


import pytest
import example


def test_can_call_existing_endpoints_of_the_API():
    try:
        detected = example.get_coordinates("Lima,Perú")
    except:
        assert False, "Exception while calling an existing function"


def test_cannot_call_nonexisting_endpoints_of_the_API():
    try:
        detected = example.something_not_existent("Lima,Perú")
        assert False, "I was able to call a non-existent function"
    except:
        pass


def test_endpoint_returns_something():
    try:
        detected = example.get_coordinates("Lima,Perú")
        assert detected is not None
    except:
        assert False, "Exception while calling an existing function"


def near(point1, point2):
    return abs(point1[0] - point2[0]) < 0.1 and abs(point1[1] - point2[1]) < 0.1


def test_the_result_is_correct_for_lima():
    # lima coordinates
    expected = -12.0463731, -77.042754
    detected = example.get_coordinates("Lima,Perú")
    assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_buenos_aires():
    # buenos aires coordinates
    expected = -34.6075682, -58.4370894
    detected = example.get_coordinates("Buenos Aires, Argentina")
    assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_quito():
    # quito coordinates
    expected = -0.2201641, -78.5123274
    detected = example.get_coordinates("Quito, Ecuador")
    assert near(detected, expected), "The result is not the expected one"


def test_the_result_is_correct_for_bogota():
    # bogota coordinates
    expected = 4.598077, -74.076102
    detected = example.get_coordinates("Bogotá, Colombia")
    assert near(detected, expected), "The result is not the expected one"


"""
algo comentario as



"""
