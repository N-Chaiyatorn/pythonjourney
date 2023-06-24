# https://sunrise-sunset.org/api
import requests

LATITUDE = 11.12
LONGITUDE = 105.45

parameters = {
    "lat":LATITUDE,
    "lng":LONGITUDE
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())