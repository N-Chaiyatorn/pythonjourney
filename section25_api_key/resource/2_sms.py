# twilio เป็น module ที่ใช้ในการส่ง sms
# เวลาใช้ต้องเข้าไปใน เว็บ twilio เเล้วพิมพ์ หมายเลขโทรศัพท์ที่เราต้องการจะส่งกับตัวต้นทางจากนั้น copy code จากที่ เว็บมันสร้สางมาให้เเล้วมาวางใน vs code
# เวลาเราจะส่งเมลให้เบอร์อืนจะยังคงส่งไม่ได้นะถ้ายังไม่ผ่านการยืนยันตัวตนระหว่างเรากับเบอร์เขาก่อน
from twilio.rest import Client
import random

g = "hello"

account_sid = 'ACb1281026ebff5f53909bdf56891972a7'
auth_token = 'd2e13427493220101845f359d7a25138'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16187423072',
  body=g,
  to='+6622359494'
)

print(message.sid)
# go back to quiz 2 and send sms if it is going to rain with next 12 hours
# check the place which are raining here https://www.ventusky.com/ 