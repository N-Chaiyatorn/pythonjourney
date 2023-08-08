import os
import requests
from tesla import Tesla
from percent_diff_stock_calculator import PercentDiffStockCalculator
from sms_sendor import SmsSendor

STOCK = "TSLA"              # symbol value.
COMPANY_NAME = "Tesla Inc"

# (check api ของราคาหุ้น เเล้วส่งมาใน sms)
## STEP 1: Use https://www.alphavantage.co (API_KEY:BQUXIFLRRZTLV1KZ)
# When STOCK price increase/decreases by 5% (จริงๆเท่าไหร่ก็ได้) between yesterday and the day before yesterday then print("Get News").

def show_send_sms_news(sms_sendor):
    """Shows user's sms massage that to will be send to their sms."""
    news_no = 0

    for massage in sms_sendor.send_sms_massage_list:
        news_no += 1
        print(f"{news_no}.):{massage}\n")

# Determine every objects.
tesla = Tesla() 
percentage_diff_stock_calculator = PercentDiffStockCalculator()
sms_sendor = SmsSendor()

# Determine every environment variables.
auth_token = os.environ.get('auth_token')
stock_api_key = os.environ.get("stock_api_key")
news_api_key = os.environ.get("news_api_key")

# Determine stock price parameters for api gets.
stock_api_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":stock_api_key

}

# Getting tesla's stock price from api get. 
response = requests.get(url = 'https://www.alphavantage.co/query?', params = stock_api_params)
stock_data = response.json()

# Determine every data for calculating and considerd days.
tesla.updating_initial_data_for_considerd_days(stock_data = stock_data)

# Calculating percentage of difference price between days in lastest days.
tesla.percentage_diff_price = percentage_diff_stock_calculator.calculating_percents_pers_days(tesla = tesla)

# Print the result of calculation.
print(f"Differrence percent of stock price between lastest days is {round(tesla.percentage_diff_price, ndigits = 2)}%\n")

# if tesla.percentage_diff_price >= 5:
#     print("gets news")
#     percent_diff_text = f"🔺{tesla.percentage_diff_price}"
# elif tesla.percentage_diff_price <= -5:
#     print("gets news")
#     percent_diff_text = f"🔻{tesla.percentage_diff_price}"

# (check หัวข้อข่าว)
## STEP 2: Use https://newsapi.org 
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# Check if percent increase or decrease by 5% then searching news and sending 3 sms massages to user's phone.
if tesla.percentage_diff_price >= 5 or tesla.percentage_diff_price <= -5:
    # Getting every tesla news from lastest days to current days.
    every_tesla_news = tesla.updating_every_news_of_tesla(news_api_key = news_api_key)

    is_percent_diff_rise_up = percentage_diff_stock_calculator.is_percent_diff_rise_up(tesla = tesla)

    # Getting percent display text.
    if is_percent_diff_rise_up:
        percent_diff_text = f"🔺{tesla.percentage_diff_price}%"
    elif not is_percent_diff_rise_up:
        percent_diff_text = f"🔻{tesla.percentage_diff_price}%"

    # Filtering 3 news to given list.
    tesla.getting_filtered_news_list(every_tesla_news = every_tesla_news)

    # Creating sms massages from 3 sms articles.
    sms_sendor.creating_sms_massage_list(tesla = tesla, stock = STOCK, percent_diff_text = percent_diff_text)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    # Sending 3 sms to user's phone.
    
    show_send_sms_news(sms_sendor = sms_sendor)
    sms_sendor.sending_sms(auth_token = auth_token)

else:
    print(f"The massage haven't been send due to percentage of stock price between days didn't reach to lower than -5% or higher than 5%.")


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

