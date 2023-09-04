import os

# สามารถ set ได้ที่ advance system setting
# use export command in terminal to create environment variable
# example: api_key=test
# environment variable คือ ตัวเเปรหรือค่าต่างๆที่เราไม่ควรจะเอามาไว้ใน code ของเราโดยตรง เช่นรหัสต่างๆ api_key ดังนั้นตัวเเปรต่างๆเหล่านี้จึงถูกเก็บไว้ในคอมเเทน
api_key = os.environ.get("auth_token")             # "API_KEY" คือ environment key ตัวนึง
# เวลาเรียกใช้ environ varia จะใช้คำสั่ง os.environ.get("ชื่อตัวเเปร environ varia ที่ต้องการ")  

print(api_key)

# bonus, other api: https://apilist.fun/