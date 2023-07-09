import os

# use export command in terminal to create environment variable
# example: api_key=test
# environment variable คือ ตัวเเปรหรือค่าต่างๆที่เราไม่ควรจะเอามาไว้ใน code ของเราโดยตรง เช่นรหัสต่างๆ api_key ดังนั้นตัวเเปรต่างๆเหล่านี้จึงถูกเก็บไว้ในคอมเเทน
api_key = os.environ.get("API_KEY")             # "API_KEY" คือ environment key ตัวนึง
# เวลาเรียกใช้ environ varia จะใช้คำสั่ง os.environ.get("ชื่อตัวเเปร environ varia ที่ต้องการ")  

print(api_key)

# bonus, other api: https://apilist.fun/

# Follow this link to define or set new  https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0