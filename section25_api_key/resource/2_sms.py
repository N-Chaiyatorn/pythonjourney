from twilio.rest import Client

account_sid = ""
auth_token = "''"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="",
    body="",
    to=""
)


# go back to quiz 2 and send sms if it is going to rain with next 12 hours
# check the place which are raining here https://www.ventusky.com/ 