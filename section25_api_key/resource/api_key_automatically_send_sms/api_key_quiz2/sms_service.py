from twilio.rest import Client
import os

class SmsService():
    def __init__(self) -> None:
        self.sms_body = f"\nIn Ladkrbang\n"

    def creating_body_text(self, rainning_time_dataframe):
        for (index, row) in rainning_time_dataframe.iterrows():
            new_text = f"In {row['date']}, {row['time']} raining will occur.\n"
            self.sms_body += new_text

    def sending_sms(self):
        account_sid = 'ACb1281026ebff5f53909bdf56891972a7'
        auth_token = os.environ.get('auth_token')
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_ = '+16187423072',
                body = self.sms_body,
                to = '+66622359494')






