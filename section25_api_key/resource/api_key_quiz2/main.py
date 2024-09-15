import requests
import os
import pandas
from geopy.geocoders import Nominatim
import datetime as dt
from data_manager import DataManager
from file_service import FileService
from sms_sendor import SmsSendor


def display_result(data_manager):
    """Print the result of weathers in next 12 hours."""
    print(f"\nThe result data is \n\n{data_manager.dataframe}")


# Input user's town.
town_name = input("Please type your town name: ")

# Determine every objects.
data_manager = DataManager()
file_service = FileService()
sms_sendor = SmsSendor()

# Getting user's town position data.
position_detection = Nominatim(user_agent = "Jotaro")
location_data = position_detection.geocode(town_name)

# Getting current time data.
current_time = dt.datetime.now()

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

# Determine dataframe column and creating in initial data dictionary.
data_manager.set_column_list(weather_data = data['hourly'][0]['weather'][0])
file_service.sets_csv_file_name()

empty_data_dict = data_manager.creating_empty_data_dict()

try:
    data_manager.dataframe = pandas.read_csv(file_service.csv_file_name)
except:
    data_manager.dataframe = pandas.DataFrame(empty_data_dict)
    data_manager.dataframe.to_csv(file_service.csv_file_name, index = False)

print(f"Your current data is \n\n{data_manager.dataframe}\n\n")

is_reset_data = data_manager.is_reset_data(file_name = file_service.csv_file_name)

if is_reset_data:
    data_manager.dataframe = pandas.DataFrame(empty_data_dict)

total_storaged_hours = 0 

# Adding data to dictionary.
for hourly_data in data['hourly']:
    data_manager.update_lastest_row_dict(weather_data_in_each_hours = hourly_data['weather'][0], time_data = current_time)
    repeatly_prohibit_rows = data_manager.getting_repeatly_dataframe()

    if repeatly_prohibit_rows.empty:
        data_manager.dataframe = pandas.concat([data_manager.dataframe, pandas.DataFrame(data_manager.lastest_row_dict)])

    total_storaged_hours += 1
    if total_storaged_hours == 12:
        break

    current_time += dt.timedelta(hours = 1)

rainning_time_dataframe = data_manager.getting_raining_time_dataframe()

if not rainning_time_dataframe.empty:
    sms_body = f"\nIn {town_name}\n"

    for (index, row) in rainning_time_dataframe.iterrows():
        new_text = f"In {row['date']}, {row['time']} raining will occur.\n"
        print(new_text)
        sms_body += new_text

    sms_sendor.sending_sms(sms_body = sms_body)
    print("The sms has been send.")

else:
    print("The sms hadn't been send.")
    
    
display_result(data_manager = data_manager)
data_manager.dataframe.to_csv(file_service.csv_file_name, index = False)