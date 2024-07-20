import requests

# get_coordinates это для получение кординаты города
def get_coordinates(city_name):
    geocode_url = f'https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1'
    response = requests.get(geocode_url)

    if response.status_code == 200:
        data = response.json()
        if data:
            lat = data[0]['lat']
            lon = data[0]['lon']
            return float(lat), float(lon)
    return None, None


def get_weather(city_name):
    lat, lon = get_coordinates(city_name)
    if lat is not None and lon is not None:
        url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m'
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                if 'hourly' in data and 'temperature_2m' in data['hourly']:
                    return {
                        'city': city_name,
                        'temperature': data['hourly']['temperature_2m'][0]
                    }
                return None
            except ValueError:
                return None
    return None
