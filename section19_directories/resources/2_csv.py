# ไฟล์ csv (comma separated value) คือ ไฟล์ที่มีลักษณะเป็นตารางที่เเยกเป็นเเถวกับหลักโดยเเต่ละหลักในตารางจะถูกเเยกกันด้วย comma

# with open("/Gittest/Python study/pythonjourney/section19_directories/resources/transaction.csv") as data_file:
#     data = data_file.read()
#     print(data)



# import csv

# with open("/Gittest/Python study/pythonjourney/section19_directories/resources/transaction.csv") as data_file:
#     data = csv.reader(data_file)       # csv.reader จะทำหน้าที่สร้าง list เเต่ละเเถว  (list ซ้อน list)        
#     for row in data:
#         print(row)



import pandas #ค่อนข้างสำคัญ 

data = pandas.read_csv("/Gittest/python_learning_after_sec_21/pythonjourney/section19_directories/resources/transaction.csv")
print(data["unitsSold"][4])