
# NAME
test_geoapi - Módulo de pruebas para geoapi.py

# DESCRIPTION
Este módulo contiene pruebas unitarias para verificar el funcionamiento de las funciones en geoapi.py.

# FUNCTIONS
    
## **distance_near(detected_distance, expected_distance, tolerance=50)**
Función para verificar si la distancia detectada está dentro de un margen de error con respecto a la distancia esperada.
        
### Args:
    detected_distance (float): La distancia calculada entre dos puntos.
    expected_distance (float): La distancia esperada entre los dos puntos.
    tolerance (float): El margen de error permitido. Default es 50 km.
        
### Returns:
    bool: True si la distancia detectada está dentro del margen de error, False en caso contrario.
    
## **near(point1, point2)**
Función para verificar si dos puntos son cercanos, esta tiene un margen de error de 0.1, lo que significa
que si la diferencia entre los puntos es menor a 0.1, se consideran iguales.
        
### Args:
    point1 (tuple): Primer punto a comparar.
    point2 (tuple): Segundo punto a comparar.
        
### Returns:
    bool: True si los puntos son cercanos, False en caso contrario.

## Tests

### 1    
    test_can_call_distance_endpoint()
        Test para probar si se puede llamar al endpoint de distancia de la API.
        
        Args:
            None
        
        Returns:
            None

### 2
    
    test_can_call_existing_endpoints_of_the_API()
        Test para probar si se puede llamar a los endpoints existentes de la API.
        
        Args:
            None
        
        Returns:
            None
    
### 3

    test_cannot_call_nonexisting_endpoints_of_the_API()
        Test para probar si no se puede llamar a los endpoints no existentes de la API.
        
        Args:
            None
        
        Returns:
            None
    
### 4

    test_distance_endpoint_returns_something()
        Test para probar si el endpoint de distancia retorna algo.
        
        Args:
            None
        
        Returns:
            None

### 5
    
    test_endpoint_returns_something()
        Test para probar si el endpoint retorna algo.
        
        Args:
            None
        
        Returns:
            None

### 6
    
    test_the_distance_is_correct()
        Test para verificar si la distancia obtenida entre Lima, Perú y Buenos Aires, Argentina es correcta.
        
        Args:
            None
        Returns:
            None

### 7
    
    test_the_result_is_correct_for_bogota()
        Test para verificar si las coordenadas obtenidas para Bogotá, Colombia son correctas.
        
        Args:
            None
        Returns:
            None

### 8
    
    test_the_result_is_correct_for_buenos_aires()
        Test para verificar si las coordenadas obtenidas para Buenos Aires, Argentina son correctas.
        
        Args:
            None
        Returns:
            None

### 9
    
    test_the_result_is_correct_for_lima()
        Test para verificar si las coordenadas obtenidas para Lima, Perú son correctas.
        
        Args:
            None
        Returns:
            None

### 10
    
    test_the_result_is_correct_for_quito()
        Test para verificar si las coordenadas obtenidas para Quito, Ecuador son correctas.
        
        Args:
            None
        Returns:
            None
