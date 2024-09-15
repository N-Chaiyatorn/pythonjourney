# API is a set of commands, functions, protocols, objects, 
# that programmers can use to create software or interact with external system
# API คือรูปเเบบการขอข้อมูลหรือ request ข้อมูลจากเว็บต่างๆ โดยข้อมูลที่ได้กลับมาจะเป็นในรูปไฟล์ json

# ISS Location API Doc: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# JSON Viewer Chrome Plugin: https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh


# requests module doc: https://docs.python-requests.org/en/latest/
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")  # get เป็นคำสั่งที่ใช้ request ข้อมูลจากตัว url ปลายทาง

print(response)     # Output is <Response [200]>  หมายถึงว่า response จากการ request มันสำเร็จ     
# [200] ==. คือ response code


# Response Codes 
# 1XX: Hold On      การขอ request ยังไม่สำเร็จ
# 2XX: Success      การขอ request สำเร็จ
# 3XX: Redirect         การเด้งหน้าอื่นโดยอัตโนมัติ ยังสำเร็จ
# 4XX: Client fault
# 5XX: Server fault
# https://www.webfx.com/web-development/glossary/http-status-codes/

print(response.status_code)
# response.raise_for_status()           เป็นตัวที่ทำให้โปรเเกรมเเสดง error เเละหยุดทำงานเมื่อ response codes อยู่ในขอบเขตที่เกิด error (ก็คือขอบเขต 400-599)
# เพราะเนื่องโปรเเกรมจะยัง work ต่อถึงเเม้ว่า request code จะเป้น 400-599 เเต่ถ้าเราไม่ raise_for_status โปรเเกรมจะทำงานต่อไปโดยที่เราไม่รู้เลยว่าเกิด error
# # where is the ISS in world map? https://www.latlong.net/Show-Latitude-Longitude.html
data = response.json()
print(data)