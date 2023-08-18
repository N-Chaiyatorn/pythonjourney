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
import time
from user import User
from iss_satellite import IssSatellite
from date_utils import DateUtils

def is_iss_overhead(iss_satellite, user):
    
    magnitude_of_distance_in_latitude = abs(iss_satellite.latitude - user.latitude)
    magnitude_of_distance_in_longitude = abs(iss_satellite.longitude - user.longitude)

    if magnitude_of_distance_in_latitude <= 5 and magnitude_of_distance_in_longitude <= 5:
        return True
    else:
        return False

def is_night(sunrise_time, sunset_time, now):
    # after 6pm-24pm-5am
    sunrise_datetime = dt.datetime.strptime(sunrise_time, "%I:%M:%S %p")
    sunset_datetime = dt.datetime.strptime(sunset_time, "%I:%M:%S %p")

    if now.time() < sunrise_datetime.time() or now.time() > sunset_datetime.time():
        return True
    else:
        return False
    
def iss_detecting_program():
    
    date_utils = DateUtils()
    user = User()
    iss_satellite = IssSatellite()

    user.set_user_location()
    user.set_user_current_position()
    iss_satellite.set_current_position()

    now = dt.datetime.now()
    now_date = date_utils.filtered_date_format_to_correct_format(now = now)

    parameters = {
        "lat":user.latitude,
        "long":user.longitude,
        "date":now_date
        }

    sunrise_sunset_data_response = requests.get(url = "https://api.sunrise-sunset.org/json?", params=parameters)
    sunrise_sunset_data = sunrise_sunset_data_response.json()

    is_night_time = is_night(sunrise_time = sunrise_sunset_data['results']['sunrise'], sunset_time = sunrise_sunset_data['results']['sunset'], now = now)
    is_iss_over_user_head = is_iss_overhead(iss_satellite = iss_satellite, user = user)

    user.print_user_current_position()
    iss_satellite.print_current_position()
    print(f"\n This time is {now.time()} and today sunrise time is {sunrise_sunset_data['results']['sunrise']}, sunset time is {sunrise_sunset_data['results']['sunset']}")

    if is_night_time and is_iss_over_user_head:
        print("\nYou can see Iss satellite now.\nYou should don't miss this.")
        my_email = "pan289277@gmail.com"
        password = "xvnpwhutejppterx"
        
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user = my_email, password = password)

        connection.sendmail(from_addr = my_email, to_addrs = my_email, msg = "Subject:You can see Iss satellite now!!\n\nThis time you can see Iss satellite in the sky at your location now.\nDon't miss them!!!.")

    else:
        print("\nYou can't see Iss satellite now.")


while True:
    iss_detecting_program()
    time.sleep(5)