# https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

# use pandas to make the squirrel data to be like squirrel_count.csv file

import pandas

# Reading csv data file.
squirrels_data_frame = pandas.read_csv("/Gittest/Python study/pythonjourney/section19_directories/project_squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv", encoding = "ISO-8859-1")

# Filtering and sorting fur color into new filtered dataframe.
gray_squirrels_data_frame = squirrels_data_frame[squirrels_data_frame["Primary Fur Color"] == "Gray"]
cinnamon_squirrels_data_frame = squirrels_data_frame[squirrels_data_frame["Primary Fur Color"] == "Cinnamon"]
black_squirrels_data_frame = squirrels_data_frame[squirrels_data_frame["Primary Fur Color"] == "Black"]

# Create new dictionary that contains every filtered data.
counted_squirrels_data = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[len(gray_squirrels_data_frame["Primary Fur Color"]), len(cinnamon_squirrels_data_frame["Primary Fur Color"]), len(black_squirrels_data_frame["Primary Fur Color"])]
}

# Create new data frame.
counted_squirrels_data_frame = pandas.DataFrame(counted_squirrels_data)
print(counted_squirrels_data_frame)

# Create new filtered color csv file.
counted_squirrels_data_frame.to_csv("counted_squirrels_data.csv")