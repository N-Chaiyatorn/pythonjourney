# online json viewer https://jsonviewer.stack.hu/

# API key คือการ request ข้อมูลคนอื่นโดยกรณ๊นี้ผู้อื่นเเต่บางข้อมูลคนให้ข้อมูลก็อยากจะจำกัดการให้ข้อมูลด้วยวิธีต่างๆดังนั้นการที่เราจะเข้าถึงได้ก็จำเป็นจะต้องยืนยันตัวตนผ่าน API key ของตัวเราเองที่ได้จากการสมัครเว็บต้นทาง
# API key คือ parameter ของ API ที่ใช้ในการยืนยันตัวตนของคนขอ request ข้อมูลเพื่อให้คนให้ข้อมูลมาเก็บค่าข้อมูลได้สะดวก

# quiz 1
# 1. Make a request to the One Call API
# 2. print HTTP status code and respponse
# 3. check out the response in the json viewer
# 4. check out the hourly weather in next 48 hours

import requests
import os
import pandas
from geopy.geocoders import Nominatim
import datetime as dt

# Determine class named 'DataManager' to manage and update data.

class DataManager():
    def __init__(self):
        self.data_dict = {}
        self.column_list = []
        self.dataframe = None

    def gets_column_list(self, weather_data):
        """Determine dataframe column."""
        self.column_list.append('date')
        self.column_list.append('time')

        for weather_col in weather_data:
            self.column_list.append(weather_col)

    def creating_data_dict(self):
        """Creating initial data dictionary."""
        self.data_dict = {column:[] for column in self.column_list}

    def update_data_dict(self, weather_data_in_each_hours, time_data):
        """Update data dictionary in each hour."""
        self.data_dict['date'].append(str(time_data.date()))
        self.data_dict['time'].append(str(time_data.hour) + ':00')

        for col in weather_data_in_each_hours:
            self.data_dict[col].append(weather_data_in_each_hours[col])

    def creating_dataframe(self):
        self.dataframe = pandas.DataFrame(self.data_dict)

def display_result(data_manager):
    """Print the result of weathers in next 48 hours."""
    print(f"The result is \n\n{data_manager.dataframe}")


# Input user's town
town_name = input("Please type your town name: ")

# Determine 'data_manager' object
data_manager = DataManager()

# Getting user's town position data.
position_detection = Nominatim(user_agent = "...")
location_data = position_detection.geocode(town_name)

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

# Print status code.
print(f"respond of request sending is {response}")
print(f"Status code is {response.status_code}")


data = response.json()

# Determine time variable to store every hours in time data.
time_data = now

# Determine dataframe column and creating in initial data dictionary.
data_manager.gets_column_list(weather_data = data['hourly'][0]['weather'][0])
data_manager.creating_data_dict()

# Adding data to dictionary.
for hourly_data in data['hourly']:
    data_manager.update_data_dict(weather_data_in_each_hours = hourly_data['weather'][0], time_data = time_data)
    time_data += dt.timedelta(hours = 1)

# Creating dataframe and print the result.
data_manager.creating_dataframe()
display_result(data_manager = data_manager)