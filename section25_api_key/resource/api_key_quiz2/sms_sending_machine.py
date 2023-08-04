from twilio.rest import Client

class SmsSendingMachine():
        
    def sending_sms(self, sms_body):
        account_sid = 'ACb1281026ebff5f53909bdf56891972a7'
        auth_token = '30f8a37ece7d32d3a1f6d3a108becccf'
        client = Client(account_sid, auth_token)
        message = client.messages.create(from_ = '+16187423072',
                body = sms_body,
                to = '+66622359494')






