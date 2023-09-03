#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from data_manager import DataManager
import datetime as dt
import smtplib
import requests
import os
from twilio.rest import Client
from csv_service import CsvService
import pandas
from json_service import JsonService

def status_code_value_error_occur():
    raise ValueError("Api searching process are incomplete or get error.")

def validate_status_code(status_code):
    if status_code < 200 or status_code >= 300:
        raise ValueError() 

def is_key_exist(key, dict):
    if key in dict.keys():
        return True
    else:
        return False

def get_date_to(date_from, month_delta):
    date_to_year = date_from.year
    date_to_month = date_from.month + month_delta

    if date_to_month > 12:
        date_to_month -= 12
        date_to_year = date_from.year + 1

    return date_from.replace(month = date_to_month, year = date_to_year)

def get_client_for_sms(account_sid):
    auth_token = os.environ.get('auth_token')

    return Client(account_sid, auth_token)

# Determine every object.
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()
data_manager = DataManager()
json_service = JsonService()
csv_service = CsvService()

now = dt.datetime.now()

# Determine object 'client' for sending sms.
ACCOUNT_SID = 'ACb1281026ebff5f53909bdf56891972a7'
client = get_client_for_sms(account_sid = ACCOUNT_SID)

# Determine connection object for send email when error occur.
my_email = "pan289277@gmail.com"
password = "xvnpwhutejppterx"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(my_email, password)

STARTING_POINT_CITY = "Bangkok"

# Get json and csv file path.
json_file_path = "/Gittest/python_learning_after_sec_21/pythonjourney/section27_flight_deal_finder/send_sms_flight_data.json"
csv_file_path = json_file_path.replace("json", "csv")

# Set file path from given file path.
json_service.set_file_path(file_path = json_file_path)
csv_service.set_file_path(csv_file_path = csv_file_path)

# Read csv file and get current dataframe.
try:
    flight_data.sms_flights_dataframe = csv_service.get_csv_file_data()
except FileNotFoundError:
    flight_data.set_sms_flights_dataframe_to_empty()
except pandas.errors.EmptyDataError:
    flight_data.set_sms_flights_dataframe_to_empty()
    csv_service.update_data_to_csv(data = flight_data.sms_flights_dataframe)

# Get kiwi api key
kiwi_api_key = os.environ.get("kiwi_api_key")

# Determine parameter for api get.
kiwi_headers = {
    "apikey":kiwi_api_key
}

body = {
        "term":STARTING_POINT_CITY,
        "location_types":"city"
    }

# Get api request.
response = requests.get(url = "https://api.tequila.kiwi.com/locations/query", params = body, headers = kiwi_headers)


# ควรจะหาวิธีเขียนโค้ดให้สั้นที่สุด 
# 
# 
# 
# 
# try:
#     response.raise_for_status()
# except:
#     connection.sendmail(from_addr = my_email, to_addrs = my_email, msg = f"Subject:Api search are failed.\nplease check your code or calling to address {my_email}.")
#     status_code_value_error_occur()

try:
    validate_status_code(status_code = response.status_code)
except:
    connection.sendmail(from_addr = my_email, to_addrs = my_email, msg = f"Subject:Api search are failed.\nplease check your code or calling to address {my_email}.")
    status_code_value_error_occur()
        
flight_data.set_starting_city_data(city_name = STARTING_POINT_CITY, iata_code = response.json()["locations"][0]["code"])
response = data_manager.get_google_sheet_data()

try:
    validate_status_code(status_code = response.status_code)
except:
    connection.sendmail(from_addr = my_email, to_addrs = my_email, msg = f"Subject:Api search are failed.\nplease check your code or calling to address {my_email}.")
    status_code_value_error_occur()

# Set endpoint_city_data from every data that get from google sheet.
flight_data.set_endpoint_city_data(data = response.json()["prices"])

# Gets and put iata code of endpoint city that determined in google sheet.
for row in flight_data.endpoint_city_data:

    if row["iataCode"] == "":

        # Determine parameter for api searching location data
        body = {
            "term":row["city"],
            "location_types":"city"
            }

        # Searching city that you have defined.
        response = flight_search.searching_endpoint_city(kiwi_headers = kiwi_headers, body = body)

        try:
            validate_status_code(status_code = response.status_code)
        except:
            connection.sendmail(from_addr = my_email, to_addrs = my_email, msg = f"Subject:Api search are failed.\nplease check your code or calling to address {my_email}.")
            status_code_value_error_occur()

        # Determine row_num for define real row num in google sheet.
        row_num = row["id"]

        endpoint_list_index = row_num - 2

        # Get iata code from data that you have import from api get and update data to endpoint city data dict.
        city_iata_code = data_manager.get_iata_code(city_data = response.json(), city_name = row["city"])
        flight_data.set_iata_to_endpoint_city_data(iata_code = city_iata_code, index = endpoint_list_index)

        # Set body parameter for api put.
        data_manager.set_editing_data_format(editing_col = "iataCode", new_data = city_iata_code)
        body = data_manager.get_put_body_params()

        # Api put.
        response = data_manager.put_data(row_num = row_num, body = body)

        try:
            validate_status_code(status_code = response.status_code)
        except:
            connection.sendmail(from_addr = my_email, to_addrs = my_email, msg = f"Subject:Api search are failed.\nplease check your code or calling to address {my_email}.")
            status_code_value_error_occur()

# Get date_from and date_to that define the range of departure time.
date_from = (now + dt.timedelta(days = 1)).date()
date_to = (date_from + pandas.DateOffset(months = 6)).date()

for endpoint_city in flight_data.endpoint_city_data:

    # Set body parameter.
    body = {
        "fly_from":"BKK",
        "fly_to":endpoint_city["iataCode"],
        "date_from":dt.datetime.strftime(date_from, "%d/%m/%Y"),
        "date_to":dt.datetime.strftime(date_to, "%d/%m/%Y"),
        "return_from":dt.datetime.strftime(date_from, "%d/%m/%Y"),
        "return_to":dt.datetime.strftime(date_to, "%d/%m/%Y"),
        "curr":"USD",
        "max_stopovers":0
    }

    # Searching for flight trips.
    response = flight_search.searching_flight(body = body, headers = kiwi_headers)

    try:
        validate_status_code(status_code = response.status_code)
    except:
        connection.sendmail(from_addr = my_email, to_addrs = my_email, msg = f"Subject:Api search are failed.\nplease check your code or calling to address {my_email}.")
        status_code_value_error_occur()

    # Set response.json() data to 'every_flight_for_each_city'.
    flight_data.set_every_flight_for_each_city(city_flights = response.json()["data"])

    # Filter every trips that the trip duration is around 7 days to 28 days. 
    available_total_days_trip_flights = flight_data.get_available_total_days_trip_flights()

    # Filter every trips that total price is lower than lowestprice that you have defined in google sheet.
    available_flights = flight_data.filter_the_lowerprice_trips(available_total_days_trip_flights = available_total_days_trip_flights, endpoint_city = endpoint_city)

    # Check is trips is available.
    is_send_notification = notification_manager.is_send_notification(the_amount_of_available_flights = len(available_flights))

    if is_send_notification:
        # Get only one flight from every available flight.
        send_sms_flight = notification_manager.get_randomaly_notification_flight(available_flight_list = available_flights)

        # Get notification message.
        notification_message = notification_manager.get_notification_message(send_sms_flight = send_sms_flight)

        # Send sms.
        notification_manager.sending_notification(client = client, body = notification_message)

        # Set sms send time and date to record into csv and json file.
        send_sms_flight["time"] = str(now.time())
        send_sms_flight["date"] = str(dt.datetime.strftime(now.date(), "%Y-%m-%d"))
        
        # Update recorded send sms flight. 
        flight_data.update_sms_flights_dataframe(flight = send_sms_flight)

    # Display sms result for each endpoint city trip.
    notification_manager.display_notification_status(start_city = STARTING_POINT_CITY, endpoint_city = endpoint_city["city"], is_send_notification = is_send_notification)

# Update data to csv and json file.
csv_service.update_data_to_csv(data = flight_data.sms_flights_dataframe)
json_service.dump_json_file(data = flight_data.sms_flights_dataframe.to_dict())

print(f"The result data is:\n\n{flight_data.sms_flights_dataframe}")