# https://docs.python.org/3/library/json.html

# Most common functions
"""
Write: json.dump()
Read: json.load()
"""

import json
# json คือ รูปเเบบไฟล์รูปเเบบหนึ่งที่เอาไว้เก็บข้อมูลในรูปเเบบของ datastructure

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
    data = json.load(file)          #json.load เป็น method ในการอ่านไฟล์ json เเละเเปลงข้อมูลเป็น dict 
    print(data)
    print(type(data))

    new_dict = {
        "Ford": {
            "color": "red",
            "year": 2017
        },
    }
    data.update(new_item)

# คำสั่ง with open คือ สิ่งต่างๆ ที่เกิดขึ้นเช่นตัวเเปรต่างๆ ถึงจะดูเหมือนว่ามี indentation เเต่ว่า
# สิ่งต่างๆ เหล่านั้นมันก็คือการประกาศตัวเเปรเเบบปกติเลย

with open("../data.json", "w") as file:
    json.dump(data, file, indent=4)  # คำสั่ง dump มีไว้เขียน data ที่เราต้องการโดยการเขียนทับเข้าไปในไฟล์ที่กำหนดไว้
