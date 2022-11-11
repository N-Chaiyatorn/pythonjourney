""" Python Lists """

#               -3      -2        -1 
#                0       1         2
car_brands = ["ford", "toyota", "honda"]

# think of the index as offset
# print(car_brands[1])

"""Negative list index"""
# print(car_brands[-1])

"""Change items in the list"""
# car_brands[0] = "porsche"

# print(car_brands)

"""add new item in the list"""
# car_brands.append("nissan")
# print(car_brands)

"""add item list to the list"""
# car_brands.extend(["lamborghini", "isuzu"])
# print(car_brands)

"""index out of range error"""
# print(car_brands[10])

"""get list length"""
# print(len(car_brands))

"""nested list"""
# vehicle_lists = [car_brands, ["suzuki", "vespa"]]

"""nested list indexing"""
# print(vehicle_lists[1][0])