from twilio.rest import Client
import os
class SmsSendingMachine():
        
    def sending_sms(self, sms_body):
        account_sid = 'ACb1281026ebff5f53909bdf56891972a7'
        auth_token = os.environ.get('auth_token')
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body = sms_body,
            from_='+16187423072',
            to='+66622359494')






