import requests
import os
import pandas
from geopy.geocoders import Nominatim
import datetime as dt
from data_manager import DataManager
from sms_sending_machine import SmsSendingMachine

# Determine every objects.
data_manager = DataManager()
sms_sending_machine = SmsSendingMachine()

# Getting user's town position data.
position_detection = Nominatim(user_agent = "...")
location_data = position_detection.geocode("Ladkrabang")

# Getting current time data.
now = dt.datetime.now()

# Determine api key.
api_key = os.environ.get("weather_api_key")

# Determine api parameter.
parameter = {
    "lat":location_data.latitude,
    "lon":location_data.longitude,
    "appid":api_key,
    "exclude":["minutely","current","daily","alerts"]
}

# Getting response data from api request.
response = requests.get(url = "https://api.openweathermap.org/data/3.0/onecall?", params = parameter)

data = response.json()

# Determine time variable to store every hours in time data.
time_data = now

# Determine dataframe column and creating initial data dictionary.
data_manager.gets_column_list(weather_data = data['hourly'][0]['weather'][0])

empty_data_dict = data_manager.creating_empty_data_dict()
data_manager.dataframe = pandas.DataFrame(empty_data_dict)

total_storaged_hours = 0 

# Adding data to dictionary.
for hourly_data in data['hourly']:
    data_manager.getting_lastest_row_data_dict(weather_data_in_each_hours = hourly_data['weather'][0], time_data = time_data)
    data_manager.dataframe = pandas.concat([data_manager.dataframe, pandas.DataFrame(data_manager.lastest_row_dict)])

    total_storaged_hours += 1

    if total_storaged_hours == 12:
        break

    time_data += dt.timedelta(hours = 1)

rainning_time_dataframe = data_manager.getting_raining_time_dataframe()

# If in next 12 hours the rain will occur, so this program will send notification to user's sms.
if not rainning_time_dataframe.empty:
    sms_sending_machine.creating_body_text(rainning_time_dataframe = rainning_time_dataframe)
    sms_sending_machine.sending_sms()