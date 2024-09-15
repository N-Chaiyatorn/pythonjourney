# https://pandas.pydata.org/docs/
import pandas
import csv

# Dataframes and Series
# data = pandas.read_csv("transaction.csv")
# print(type(data))                       # The output is <class 'pandas.core.frame.DataFrame'> หมายถึงว่าตารางทั้งตารางในไฟล์ csv จะเป็น data type ที่มีชื่อว่า DataFrame
# print(type(data["unitsSold"]))          # The output is <class 'pandas.core.series.series'>           หมายถึงว่า column ที่ชื่อว่า unitsSold ในไฟล์ csv จะเป็น data type ที่มีชื่อว่า series(column เเต่ละ column ในไฟล์ จะมี data type ชื่อว่า series)


# average units sold and max units sold, using both non-pandas and pandas
# 1.ใช้ pandas หา max
# data = pandas.read_csv("/Gittest/Python study/pythonjourney/section19_directories/resources/transaction.csv")
# print(data["unitsSold"].max())

# 2.ใช้ pandas หา average            !!!!!!!
# data = pandas.read_csv("/Gittest/Python study/pythonjourney/section19_directories/resources/transaction.csv")
# units_num = data["unitsSold"].values
# additional_num = 0
# for each_num in units_num:
#     additional_num += each_num
# print(additional_num/len(units_num))

# 3.ไม่ใช้ pandas หา max
# with open("/Gittest/Python study/pythonjourney/section19_directories/resources/transaction.csv") as data_file:
#     data = csv.reader(data_file)
#     maximum_value = 0
#     for each_row in data:
#         if each_row[4] != "unitsSold" and int(each_row[4]) > maximum_value:
#             maximum_value = int(each_row[4])
#     print(maximum_value)

          

# 4.ไม่ใช้ pandas หา average
# with open("/Gittest/Python study/pythonjourney/section19_directories/resources/transaction.csv") as data_file:
#     data = csv.reader(data_file)
#     additional_num = 0
#     row = 0
#     for each_row in data:
#         if each_row[4] != "unitsSold":
#             additional_num += int(each_row[4])
#             row +=1
# print(additional_num/row)






# filter product sold = SUPA101 rows
# ถ้าจะเลือกเเค่เเถวหนึ data.productSold 
# print(data[data.productSold == "SUPA101"])


# get row that contains highest units sold
# data = pandas.read_csv("/Gittest/Python study/pythonjourney/section19_directories/resources/transaction.csv")
# print(data[data["unitsSold"] == data["unitsSold"].max()])

# create dataframe
data_dict = {
    "students": ["pan", "jean"],    #key เปรียบเสมือนชื่อของหลัก(ชื่อของหัวตาราง) เเละ  
    "scores": [90, 90]
}
data = pandas.DataFrame(data_dict)
print(data)

data.to_csv("students.csv")

# method 'concat' is used to combining two data frame to one data frame
# Ex.
# df3 = pandas.concat(df1, df2)
# 
