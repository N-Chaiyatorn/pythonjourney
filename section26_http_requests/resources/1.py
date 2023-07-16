# HTTP Requests - checkout the http_request_type.jpg
import requests

# https://pixe.la/
PIXELA_ENDPOINNT = "https://pixe.la/v1/users"
USERNAME = "Pan"
TOKEN = "asdiuqjwpasd"

# create user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINNT, json=user_params)


# create graph
# graph_endpoint = f"{PIXELA_ENDPOINNT}/{USERNAME}/graphs"

# graph_id = "graph1"

# graph_config = {
#     "id": graph_id,
#     "name": "Running Graph",
#     "unit": "m",
#     "type": "float",
#     "color": ""
# }

# response = requests.post(url=graph_endpoint, json=graph_config)


# HTTP Header
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)



# quiz 1: try to add pixel using post request

"""
datetime strftime method to change datetime to formatted string
https://www.w3schools.com/python/python_datetime.asp
today = datetime.now()
today.strftime("%Y%m%d")
"""

# quiz 2: try put and delete requests