# https://pandas.pydata.org/docs/
import pandas

# Dataframes and Series
data = pandas.read_csv("transaction.csv")
print(type(data))
print(type(data["unitsSold"]))


# average units sold and max units sold, using both non-pandas and pandas


# filter product sold = SUPA101 rows
# print(data[data.productSold == "SUPA101"])


# get row that contains highest units sold


# create dataframe
data_dict = {
    "students": ["pan", "jean"],
    "scores": [90, 90]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("students.csv")