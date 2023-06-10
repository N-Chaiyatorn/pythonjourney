# https://docs.python.org/3/library/json.html

# Most common functions
"""
Write: json.dump()
Read: json.load()
"""

import json

dictionary = {
    "Toyota": {
        "color": "black",
        "year": 2012
    },
    "Isuzu": {
        "color": "blue",
        "year": 2014
    }
}
    
new_item = {
    "Ford": {
        "color": "red",
        "year": 2017
    },
}

with open("../data.json", "r") as file:
    data = json.load(file)
    print(data)
    print(type(data))

    new_dict = {
        "Ford": {
            "color": "red",
            "year": 2017
        },
    }
    data.update(new_item)

with open("../data.json", "w") as file:
    json.dump(data, file, indent=4)
