# quiz 2: Use One Call API hourly data to check if it will rain in the next 12 hours
# hint 1: Read the api doc and try to understand how the data is structured
# hint 2: weather code https://openweathermap.org/weather-conditions#Weather-Condition-Cod

import requests
from geopy.geocoders import Nominatim
import datetime as dt
import pandas
from rain_detector import RainDetector
from data_manager import DataManager
from data_base_file_generator import DataBaseFileGenerators


def gets_highest_data_rows(data_dict):

    highest_row = 0

    for col in data_dict:
        if len(data_dict[col]) > highest_row:
            highest_row = len(data_dict[col])

    return highest_row

def gets_highest_rows_data(data_dict, highest_row, col):

    the_amount_of_includings = highest_row - len(data_dict[col])

    for add in range(the_amount_of_includings):
        data_dict[col].append("none")

    return data_dict

def gets_12_hours_clock_format(hours):
    try:
        if hours > 24:
            raise ValueError("Invalid hours value.")
        
    except ValueError:
        hours = hours - 24

    finally:
        if hours > 12 and (hours - 12) < 10:
            return "0" + str(hours - 12) + ":00 PM"
        elif (hours - 12) >= 10:
            return str(hours - 12) + ":00 PM"
        elif hours >= 10:
            return str(hours) + ":00 AM"
        elif hours >= 0:
            return "0" + str(hours) + ":00 AM"
        

position_detection = Nominatim(user_agent = "...")
location_data = position_detection.geocode("Saphan sung")
now = dt.datetime.now()   

parameter = {
    "lat":location_data.latitude,
    "lon":location_data.longitude,
    "appid":"5cb771a217c6b8f1a43a3942911178ee",
    "exclude":["minutely","current","daily","alerts"]
}

response = requests.get(url = "https://api.openweathermap.org/data/3.0/onecall?", params = parameter)

data_base_file_generator = DataBaseFileGenerators()
data_manager = DataManager()
rain_detector = RainDetector() 

data = response.json()
file_name = data_base_file_generator.gets_to_be_saved_csv_file()
data_manager.gets_dataframe_column_name_list(weather_in_hour_data = data['hourly'][0]['weather'][0])

try: 
    data_manager.current_dataframe = pandas.read_csv(file_name)
except:
    data_manager.current_dataframe = data_manager.gets_data_frame(data_dict = data_manager.create_empty_data_dict())
    data_manager.current_dataframe.to_csv(file_name, index = False)

hours = int(now.hour) 
date = str(now.date())

total_hours = 0

for hour_data in data['hourly']:
    
    if hours >= 24:
        date = str((now + dt.timedelta(days = 1)).date())
        hours = 0

    twelve_hour_clock_time = gets_12_hours_clock_format(hours = hours)

    is_rain = rain_detector.detecting(i = hour_data)

    if is_rain:
        rain_detector.display_the_result(hours = hours)

    data_manager.update_each_hour_data_dict(weather_in_hour_data = hour_data['weather'][0], twelve_hour_clock_time = twelve_hour_clock_time, date = date)
    new_row_data = data_manager.gets_data_frame(data_dict = data_manager.new_row_data_dict)

    is_same_day_and_same_hours = data_manager.is_same_day_and_same_hours()

    if not is_same_day_and_same_hours:
        data_manager.current_dataframe = pandas.concat([data_manager.current_dataframe, new_row_data])


    hours += 1
    total_hours += 1

    if total_hours > 12:
        break

data_manager.current_dataframe.to_csv(file_name, index = False)
print(f"\n Your result data is \n{data_manager.current_dataframe}")   