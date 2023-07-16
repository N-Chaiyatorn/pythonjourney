# find your latitude and longitude: https://www.latlong.net/

# Write a program to send the email to lookup if you could see the ISS

# ISS Location API Doc: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# https://sunrise-sunset.org/api

# Assumption
# 1. you can see the ISS is close if your position is within +5 or -5 degrees of the ISS position
# Your pos : 0, 0 ,Iss pos:5,-5 (Your can see)
# If  Your pos : 0, 0 ,Iss pos:10,-5 (Your can't see)
# Your pos : 0, 0 ,Iss pos:2,3 (Your can see)
# If  Your pos : 0, 0 ,Iss pos:10,100 (Your can't see)
# 2. you can only see the ISS during the night time (before sunrise time, after sunset time)

# BONUS: run the code every 60 seconds.
import requests
import datetime as dt
import smtplib
from geopy.geocoders import Nominatim
import schedule
import time
import random


USER_LOCATION = "Ladkrabang"

def is_iss_overhead(iss_satellite, user):
    magnitude_of_distance_in_latitude = ((iss_satellite.latitude - user.latitude)**2)**(1/2)
    magnitude_of_distance_in_longitude = ((iss_satellite.longitude - user.longitude)**2)**(1/2)

    if magnitude_of_distance_in_latitude <= 5 and magnitude_of_distance_in_longitude <= 5:
        return True
    else:
        return False

def is_night(sunrise_time, sunset_time, now):
    # after 6pm-24pm-5am
    sunrise_datetime = dt.datetime.strptime(sunrise_time, "%I:%M:%S %p")
    sunset_datetime = dt.datetime.strptime(sunset_time, "%I:%M:%S %p")

    if now.hour > sunset_datetime.hour or now.hour < sunrise_datetime.hour:
        return True
    elif now.hour == sunset_datetime.hour and now.minute > sunset_datetime.minute:
        return True
    elif now.hour == sunrise_datetime.hour and now.minute < sunrise_datetime.minute:
        return True
    elif now.hour == sunset_datetime.hour and now.minute == sunset_datetime.minute and now.second > sunset_datetime.second:
        return True
    elif now.hour == sunrise_datetime.hour and now.minute == sunrise_datetime.minute and now.second < sunrise_datetime.second:
        return True
    else:
        return False

class User():
    def __init__(self):
        self.latitude = None
        self.longitude = None

    def get_current_position(self):
        geolocator = Nominatim(user_agent = "...")
        location = geolocator.geocode(USER_LOCATION)
        self.latitude = location.latitude
        self.longitude = location.longitude
    
    def print_user_current_position(self, current_position):
        print(f"Now your position is {current_position}\n Latitude:{self.latitude} \n Longitude:{self.longitude}\n")
    
class TimeDetectingMachine():
    def __init__(self):
        pass
    
    def filtered_date_format_to_correct_format(self, now):
        now_date = now.years + "-" + now.month + "-" + now.day
        return now_date

    def is_date_string_format_correct(self, date):
        # YYYY-MM-DD
        date_splited_list = date.split("-")
        if len(date_splited_list[0]) == 4 and len(date_splited_list[1]) == 2 and len(date_splited_list[2]) == 2 and "-" in list(date):
            return True
        else:
            return False

class IssSatellite():
    def __init__(self):
        self.latitude = None
        self.longitude = None
    
    def get_current_position(self):
        iss_position_response = requests.get(url = "http://api.open-notify.org/iss-now.json")
        iss_information = iss_position_response.json()
        
        self.get_current_latitude(iss_information)
        self.get_current_longitude(iss_information)
    
    def get_current_latitude(self, iss_information):
        self.latitude = float(iss_information["iss_position"]["latitude"])

    def get_current_longitude(self, iss_information):
        self.longitude = float(iss_information["iss_position"]["longitude"])

    def print_current_position(self):
        print(f"Now Iss satellite position is \n Latitude:{self.latitude} \n Longitude:{self.longitude}")

def iss_detecting_program():
    my_email = "pan289277@gmail.com"
    password = "xvnpwhutejppterx"

    time_detecting_machine = TimeDetectingMachine()
    user = User()
    iss_satellite = IssSatellite()

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user = my_email, password = password)

    user.get_current_position()
    iss_satellite.get_current_position()

    now = dt.datetime.now()
    now_date = str(now.date())
    is_date_format_correct = time_detecting_machine.is_date_string_format_correct(date = now_date)

    if not is_date_format_correct:
        time_detecting_machine.filtered_date_format_to_correct_format(now = now)


    parameters = {
        "lat":user.latitude,
        "long":user.longitude,
        "date":now_date
        }

    sunrise_sunset_data_response = requests.get(url = "https://api.sunrise-sunset.org/json?", params=parameters)
    sunrise_sunset_data = sunrise_sunset_data_response.json()

    is_night_time = is_night(sunrise_time = sunrise_sunset_data['results']['sunrise'], sunset_time = sunrise_sunset_data['results']['sunset'], now = now.time())
    is_iss_over_user_head = is_iss_overhead(iss_satellite = iss_satellite, user = user)

    user.print_user_current_position(current_position = USER_LOCATION)
    iss_satellite.print_current_position()
    print(f"\n This time is {now.time()} and today sunrise time is {sunrise_sunset_data['results']['sunrise']}, sunset time is {sunrise_sunset_data['results']['sunset']}")

    if is_night_time and is_iss_over_user_head:
        print("\nYou can see Iss satellite now.\nYou should don't miss this.")
        connection.sendmail(from_addr = my_email, to_addrs = my_email, msg = "Subject:You can see Iss satellite now!!\n\nThis time you can see Iss satellite in the sky at your location now.\nDon't miss them!!!.")
    else:
        print("\nYou can't see Iss satellite now.")


schedule.every(60).seconds.do(iss_detecting_program)
while True:
    schedule.run_pending()
    time.sleep(1)


