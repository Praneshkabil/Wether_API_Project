import requests


def weather(place):

    url = f"https://nominatim.openstreetmap.org/search?q={place}&format=json"

    headers = {
        "User-Agent": "WeatherAPIProject/1.0"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if not data:
        print("Location not found")
        return

    latitude = data[0]["lat"]
    longitude = data[0]["lon"]

    url2 = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"

    response2 = requests.get(url2)
    data_2 = response2.json()

    a = data_2["current"]["temperature_2m"]
    b = data_2["current"]["wind_speed_10m"]

    return a, b


place = input("Enter a place: ")
print(weather(place))