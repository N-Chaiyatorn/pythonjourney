
from geopy.geocoders import Nominatim

class User():
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.location = None

    def set_user_location(self):
        self.location = "Ladkrabang"

    def set_user_current_position(self):
        geolocator = Nominatim(user_agent = "...")
        location = geolocator.geocode(self.location)
        self.latitude = location.latitude
        self.longitude = location.longitude
    
    def print_user_current_position(self):
        print(f"Now your position is {self.location}\n\n Latitude:{self.latitude} \n Longitude:{self.longitude}\n")