
import requests

class IssSatellite():
    def __init__(self):
        self.latitude = None
        self.longitude = None
    
    def set_current_position(self):
        iss_position_response = requests.get(url = "http://api.open-notify.org/iss-now.json")
        iss_information = iss_position_response.json()
        
        self.set_current_latitude(iss_information)
        self.set_current_longitude(iss_information)
    
    def set_current_latitude(self, iss_information):
        self.latitude = float(iss_information["iss_position"]["latitude"])

    def set_current_longitude(self, iss_information):
        self.longitude = float(iss_information["iss_position"]["longitude"])

    def print_current_position(self):
        print(f"Now Iss satellite position is \n\n Latitude:{self.latitude} \n Longitude:{self.longitude}")