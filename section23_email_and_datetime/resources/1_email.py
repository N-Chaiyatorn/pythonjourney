import smtplib

my_email = "chaiyatorn.nr@gmail.com"
password = "yknufadiuasbwglp"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email, 
    to_addrs="chaiyatorn.nr@gmail.com", 
    msg="Subject:hi\n\nEmail body"
)
connection.close()