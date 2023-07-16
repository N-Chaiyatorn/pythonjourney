# Flght deal finder project

## Program Requirements
1. Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here https://en.wikipedia.org/wiki/IATA_airport_code#Cities_with_multiple_commercial_airports).

2. Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet. You may use any city as the starting point. We're looking for only the direct flights and round trip thats return between 7 and 28 days

3. If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

4. The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g. ![](sms_example.png)

__Note: there may actually be no flights to certain destinations__

## APIs Required

Google Sheet Data Management - https://sheety.co/

Kiwi Partners Flight Search API (Free Signup, Credit Card not required) - https://partners.kiwi.com/

Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

Twilio SMS API - https://www.twilio.com/docs/sms

## Tips
- use pretty print library to print
```
from pprint import pprint 
import request

response = request.get(...)
pprint(response.json())
```

## Guideline
1. register all api above
2. Start from copying this https://docs.google.com/spreadsheets/d/1DwIEpLR7Xrppi0RKqgbOINNzjhg0lkm9bLfLTx3CKDo/edit?usp=sharing to your spreadsheet
3. try to read (get) / write (put) to the sheet using sheety api
4. try to populate city IATA code to the every city in thte sheet
5. choose your departure location and use it for the flight data api. Attach destination locations in the sheet and your departure location to the request
6. send the sms if the price is lower than the sheet
