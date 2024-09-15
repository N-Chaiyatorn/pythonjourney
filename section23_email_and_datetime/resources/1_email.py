import smtplib

# ได้มาจากการสร้าง app password ต้องไปสร้างใน google ตรงการยืนยะันตัวตนเเละความปลอดภัยก่อน
my_email = "pan289277@gmail.com"
password = "xvnpwhutejppterx"

text = input("Type text that you want to send to email: ")
reciever = input("Type your email target that you want to send: ")
connection = smtplib.SMTP("smtp.gmail.com", port=587)
# port คือ 
# Google มี ip 8.8.8.8
# www.google.com  เช่น  มี ip 148.188.8.8:80    ถ้าเปรียบเทียบเว็บเว็บเป็นเหมือนเมืองๆหนึ้่ง ip = ชื่อเมือง(148.188.8.8), port = บริการย่อยๆของเมือง(:80)
# ip = ตนของเว็บ, port = บริการย่อยๆของเว็บ
# เช่น 
# google.com:80 ==> บริการการเชื่อมต่อเว็บในรูปเเบบ HTTP website ของ google
# google.com:80 ==> บริการการเชื่อมต่อเว็บในรูปเเบบ HTTPS website ของ google
# 

# ทุกๆ web จะมี ip address เป็นของตัวมันเอง เรียกว่า dns 
connection.starttls()
connection.login(user=my_email, password=password)
for i in range(3):
    connection.sendmail(
    from_addr=my_email, 
    to_addrs=reciever, 
    msg=f"Subject:hi\n{text}")
connection.close()