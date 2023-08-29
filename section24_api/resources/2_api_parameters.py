# https://sunrise-sunset.org/api
import requests

LATITUDE = 11.12
LONGITUDE = 105.45

parameters = {
    "lat":LATITUDE,
    "lng":LONGITUDE
}

# ในเรื่องนี้เป็นการขอ request ข้อมูลโดยยิง api ไปหา server ปลายทางโดยรับบุค่า parameter ไปด้วยซึ่งตัว
# server จะนำค่า parameter ไปเข้า function คำนวณต่างๆ เพื่อ return ค่าข้อมูลให้ผู้ใช้
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())