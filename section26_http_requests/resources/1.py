# HTTP Requests - checkout the http_request_type.jpg
import requests

# https://pixe.la/
# PIXELA_ENDPOINNT = "https://pixe.la/v1/users"
# USERNAME = "pan"
# TOKEN = "gojosenseisadef"

# # create user
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=PIXELA_ENDPOINNT, json=user_params)
# print(response.text)

# parameter โดยปกติจะใช้ requests.get(params = your_param_as_dict) เเต่ parameter
# ก็อาจจะสามารถเเยกออกได้เป็น 2 ส่วน คือ
# 1. body parameter คือ parameter ที่เก็บค่าข้อมูลทั่วไปที่ส่งให้ปลายทาง
# 2. header parameter คือ parameter ที่เอาไว้ยืนยันตัวตน

# create graph
# graph_endpoint = f"{PIXELA_ENDPOINNT}/{USERNAME}/graphs"

# graph_id = "graph2"

# graph_config = {
#     "id": graph_id,
#     "name": "test_graph",
#     "unit": "m",
#     "type": "float",
#     "color": "sora"
# }

# response = requests.post(url=graph_endpoint, json=graph_config)
# print(response.text)


# HTTP Header (คือ ส่วนที่เอาไว้ยืนยันตัวตนให้กับปลายทาง หรือพวก key ที่เอาไว้ยืนยันตัวตน)
# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Gets graph details

# response = requests.get(url = graph_endpoint, headers = headers)
# print(response.text)

# posting new data to your graph

# pixel_data = {
#     "date":"20220802",
#     "quantity":"22"
# }

# response = requests.post(url = f"{graph_endpoint}/graph1", headers = headers, json = pixel_data)
# print(response.text)


# quiz 1: try to add pixel using post request

"""
datetime strftime method to change datetime to formatted string
https://www.w3schools.com/python/python_datetime.asp
# today = datetime.now()
# today.strftime("%Y%m%d")
"""

import requests
import datetime
from graph_data_manager import GraphDataManager
from pixela_graph_generators import PixelaGraphGenerators

print("Welcome to running distance record graph program for pixela.")


def gets_considered_graph_name(choice):
    """Asking user for considered graph id."""
    if choice == '2' or choice == '3':
        return input("What graph id do you want to add new data: ")
    elif choice == '4':
        return input("What graph id do you want to update existing data: ")
    elif choice == '5':
        return input("What graph id do you want to delete (If you want to delete more than one graph please seperate between each graph by space): ").split(" ")

        
def gets_users_choice():
    """Choose your choice."""
    while True:
        try:
            ask_for_choice = """What do you want to do.
Choose 1 to create new graph.
Choose 2 to add new pixel data from yesterday to exist graph.
Choose 3 Add your new pixel data with determined days.
Choose 4 to put some data to your graph (editing existing data)
Choose 5 to delete graph
Type your choice: """

            choice = input(ask_for_choice)

            if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5':
                raise ValueError()
            
        except:
            print("Invalid input.")

        else:
            return choice

def print_invalid_params_error():
    """print error by incorrect parameters."""
    print("Its seems you submit has inappropriate values, please try again!!.")

def display_result(response):
    """Display result from pixela response."""
    print(f"Your graph status is {response.text}")

PIXELA_ENDPOINNT = "https://pixe.la/v1/users"
USERNAME = "pan"
TOKEN = "gojosenseisadef"
GRAPH_BODY_EDITING_CHOICE = ["name", "unit", "color"]
GRAPH_BODY_TITLE = ["id", "name", "type", "unit", "color"]

# Define every object.
pixela_graph_generators = PixelaGraphGenerators()
graph_data_manager = GraphDataManager()

# Gets user's choice.
choice = gets_users_choice()

# user_params = {
#         "token": TOKEN,
#         "username": USERNAME,
#         "agreeTermsOfService": "yes",
#         "notMinor": "yes"
#     }

# response = requests.post(url=PIXELA_ENDPOINNT, json=user_params)

# Determine headers parameter.
headers = {
        "X-USER-TOKEN": TOKEN
    }

# Determine graph url.
graph_url = f"{PIXELA_ENDPOINNT}/{USERNAME}/graphs"

if choice == '1':
    while True:
        try:
            # Getting graph config value.
            graph_data_manager.determine_graph_config_value(graph_config_keys_list = GRAPH_BODY_TITLE, choice = choice)

            # Creating new graph by api post.
            response = pixela_graph_generators.creating_new_graph(headers = headers, graph_data_manager = graph_data_manager, graph_url = graph_url)

            # Display result.
            display_result(response = response)

            if response.status_code < 200 or response.status_code >= 300:
                raise ValueError()
        
        except:
            print_invalid_params_error()

        else:
            break
    

elif choice == '2':
    while True:
        try:
            # Asking for considered graph.
            graph_id = gets_considered_graph_name(choice = choice)

            # Getting current time.
            now = datetime.datetime.now() - datetime.timedelta(days = 1)

            # Determine graph config.
            graph_data_manager.graph_config["date"] = now.strftime("%Y%m%d")
            graph_data_manager.graph_config["quantity"] = input("Type your distance that you runned yesterday: ")

            # Updating new pixel by api post.
            response = requests.post(url = f"{graph_url}/{graph_id}", json = graph_data_manager.graph_config, headers = headers)

            # Display result.
            display_result(response = response)

            if response.status_code < 200 or response.status_code >= 300:
                raise ValueError()
        
        except:
            print_invalid_params_error()

        else:
            break

elif choice == '3':
    while True:
        try:
            # Asking for considered graph.
            graph_id = gets_considered_graph_name(choice = choice)

            # Determine graph config.   
            graph_data_manager.graph_config["date"] = input("Type date that you have runned in (YYYYMMDD): ")
            graph_data_manager.graph_config["quantity"] = input("Type your distance that you runned: ")

            # Updating new pixel by api post.
            response = requests.post(url = f"{graph_url}/{graph_id}", json = graph_data_manager.graph_config, headers = headers)

            # Display result.
            display_result(response = response)

            if response.status_code < 200 or response.status_code >= 300:
                raise ValueError()
        
        except:
            print_invalid_params_error()

        else:
            break


# quiz 2: try put and delete requests
elif choice == '4':
    while True:
        try:
            # Asking for considered graph.
            graph_id = gets_considered_graph_name(choice = choice)

            # Asking user for editing.
            edited_title_list = graph_data_manager.asking_user_for_editing_choice(graph_body_editing_choice = GRAPH_BODY_EDITING_CHOICE)

            # Getting graph config value.
            graph_data_manager.determine_graph_config_value(graph_config_keys_list = edited_title_list, choice = choice)

            # Editing exist data by api put.
            response = requests.put(url = f"{graph_url}/{graph_id}", json = graph_data_manager.graph_config, headers = headers)

            # Display result.
            display_result(response = response)

            if response.status_code < 200 or response.status_code >= 300:
                raise ValueError()
        
        except:
            print_invalid_params_error()

        else:
            break

elif choice == '5':
    while True:
        try:
            # Asking for considered graph.
            deleted_graphs_id_list = gets_considered_graph_name(choice = '5')

            # Deleting graph.
            for deleted_graphs_id in deleted_graphs_id_list:
                response = requests.delete(url = f"{graph_url}/{deleted_graphs_id}", headers = headers)
                
                if response.status_code < 200 or response.status_code >= 300:
                    raise ValueError()

        except:
            print("Please try again!!!")

        else:
            print("___Your deleted has been completed___")
            break
