# API is a set of commands, functions, protocols, objects, 
# that programmers can use to create software or interact with external system


# ISS Location API Doc: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# JSON Viewer Chrome Plugin: https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh


# requests module doc: https://docs.python-requests.org/en/latest/
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

print(response)


# Response Codes 
# 1XX: Hold On 
# 2XX: Success 
# 3XX: Redirect
# 4XX: Client fault
# 5XX: Server fault
# https://www.webfx.com/web-development/glossary/http-status-codes/

print(response.status_code)
# response.raise_for_status()

# where is the ISS in world map? https://www.latlong.net/Show-Latitude-Longitude.html
data = response.json()
print(data)