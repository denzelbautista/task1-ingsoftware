import requests

def get_coordinates(query):
    api_url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json"
    headers = {
        'User-Agent': 'Testing App'
    }
    response = requests.get(api_url, headers=headers)
    response_data = response.json()
    
    if not response_data:
        raise HTTPException(status_code=404, detail="City not found")
    
    return float(response_data[0]['lat']), float(response_data[0]['lon'])
