# NAME
geoapi - Módulo geoapi.py

# DESCRIPTION
Este módulo contienes las rutas 

    geoapi/coordinates/{cityname}
y 

    geoapi/distance/{lat1_lon1}/{lat2_lon2} 
con las funciones 

    get_coordinates 
    
y 

    get_distance respectivamente.

# FUNCTIONS

## **get_coordinates(city_country)**
Este endpoint se encarga de obtener las coordenadas de una ciudad a partir de una consulta a la api de openstreetmap.
        
### Endpoint:
    /geoapi/coordinates/{city_country}
        
### Args:
    city_country (str): Ciudad a buscar en formato "ciudad, pais" o "pais, ciudad".
        
### Returns:
    json: json con las coordenadas de la ciudad en las claves "lat" y "lon".
    
## **get_distance(lat1_lon1, lat2_lon2)**
Este endpoint se encarga de obtener la distancia entre dos puntos geográficos
utilizando la libreria geopy para facilitar el cálculo.

### Endpoint:
    /geoapi/distance/{lat1_lon1}/{lat2_lon2}
            
### Args:
    lat1_lon1 (str): Coordenadas del primer punto en formato "latitud, longitud".
    lat2_lon2 (str): Coordenadas del segundo punto en formato "latitud, longitud".
        
### Returns:
    json: json con la distancia en la clave "distance" y las unidades en la clave "units".


