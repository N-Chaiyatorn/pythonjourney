from twilio.rest import Client
import os

class SmsSendor():
    def __init__(self):
        self.send_sms_massage_list = []

    def creating_sms_massage_list(self, tesla, stock, percent_diff_text):
        for news in tesla.filtered_news_list:
            news_article = f"""
{stock}:{percent_diff_text}
Headline:{news["title"]}
description:{news["description"]}"""
    
            self.send_sms_massage_list.append(news_article)

    def sending_sms(self, auth_token):
        account_sid = 'ACb1281026ebff5f53909bdf56891972a7'
            
        client = Client(account_sid, auth_token)
        sms_number = 1
        for sms_massage in self.send_sms_massage_list:
            massage = client.messages.create(
                from_ = '+16187423072',
                body = sms_massage,
                to='+66622359494')

            print(f"~~~Massage number {sms_number} sending successful~~~\nYou can check some news on you sms in your devices.")
            sms_number += 1
        
            
            


