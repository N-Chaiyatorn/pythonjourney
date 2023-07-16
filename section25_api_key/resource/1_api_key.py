# online json viewer https://jsonviewer.stack.hu/

# API key คือการ request ข้อมูลคนอื่นโดยกรณ๊นี้ผู้อื่นเเต่บางข้อมูลคนให้ข้อมูลก็อยากจะจำกัดการให้ข้อมูลด้วยวิธีต่างๆดังนั้นการที่เราจะเข้าถึงได้ก็จำเป็นจะต้องยืนยันตัวตนผ่าน API key ของตัวเราเองที่ได้จากการสมัครเว็บต้นทาง
# API key คือ parameter ของ API ที่ใช้ในการยืนยันตัวตนของคนขอ request ข้อมูลเพื่อให้คนให้ข้อมูลมาเก็บค่าข้อมูลได้สะดวก

# quiz 1
# 1. Make a request to the One Call API
# 2. print HTTP status code and respponse
# 3. check out the response in the json viewer
# 4. check out the hourly weather in next 48 hours

# import requests
# from geopy.geocoders import Nominatim
# from datetime import datetime

# position_detection = Nominatim(user_agent = "...")
# location_data = position_detection.geocode("Ladprao")
# now = datetime.now()

# parameter = {
#     "lat":location_data.latitude,
#     "lon":location_data.longitude,
#     "appid":"5cb771a217c6b8f1a43a3942911178ee",
#     "exclude":["minutely","current","daily","alerts"]
# }

# response = requests.get(url = "https://api.openweathermap.org/data/3.0/onecall?", params = parameter)
# print(f"respond of request sending is {response}")
# print(f"Status code is {response.status_code}")
# data = response.json()
# print(data)

# print(f"The weather in next 48 hours is: ")

# hours = int(now.hour)

# for i in data['hourly']:
#     if hours >= 24:
#         hours = 0
#     print(f"\nThe weather in {hours} is:\n {i['weather']}")
#     hours += 1




# quiz 2: Use One Call API hourly data to check if it will rain in the next 12 hours
# hint 1: Read the api doc and try to understand how the data is structured
# hint 2: weather code https://openweathermap.org/weather-conditions#Weather-Condition-Cod

import requests
from geopy.geocoders import Nominatim
from datetime import datetime
import pandas



def gets_12_hours_clock_format(hours):
    try:
        if hours > 24:
            raise ValueError("Invalid hours value.")
    except ValueError:
        hours = hours - 24
    finally:
        if hours > 12:
            return str(hours - 12) + ":00"
        elif hours < 10:
            return "0" + str(hours) + ":00"
    
class DataBaseFileGenerators():
    def __init__(self):
        self.data_dict = {}
        self.data_frame = None

    def filtering_data_frame(self):
        pass
    
    def get_data_frame(self):
        try:
            self.data_frame = pandas.DataFrame(self.data_dict)
        except:
            pass


    def update_data_dict(self, weather_data_list):
        for parameter in weather_data_list:
            try:
                self.data_dict[parameter].append(weather_data_list[parameter])
            except:
                self.data_dict[parameter] = [weather_data_list[parameter]]

    def creating_csv_file(self):
        pass

    def creating_json_file(self):
        pass
        
class RainDetector():
    def __init__(self):
        pass

    def detecting(self, i):
        if i['weather'][0]['id'] >= 500 and i['weather'][0]['id'] < 600:
            return True
        else:
            return False
        
    def display_the_result(self, hours, is_rain):
        if is_rain:
            print(f"\nIn {hours}.00, rain will occur.\n")
        else:
            print(f"\nIn {hours}.00, rain will not occur.\n")


position_detection = Nominatim(user_agent = "...")
location_data = position_detection.geocode("Saphan sung")
now = datetime.now()   
rain_detector = RainDetector()     

parameter = {
    "lat":location_data.latitude,
    "lon":location_data.longitude,
    "appid":"5cb771a217c6b8f1a43a3942911178ee",
    "exclude":["minutely","current","daily","alerts"]
}


response = requests.get(url = "https://api.openweathermap.org/data/3.0/onecall?", params = parameter)
data = response.json()

hours = int(now.hour) 
total_hours = 0
print(data)
# for i in data['hourly']:
#     if hours >= 24:
#         hours = 0

#     twelve_hour_clock_time = gets_12_hours_clock_format(hours = hours)

#     print(f"\nThe weather in {twelve_hour_clock_time} is: ")

#     is_rain = rain_detector.detecting(i = i)
#     rain_detector.display_the_result(hours = hours, is_rain = is_rain)

#     hours += 1
    
#     total_hours += 1

#     if total_hours > 12:
#         break

    