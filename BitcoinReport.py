#small project for any crypto currency report 
"""
for inquiry and support contact us 
1. akrm74ali@gmail.com
2. thawdanalsanaei@gmail.com
"""
import requests
import time

#glopal variables

api_key = "Your API Key" #https://coinmarketcap.com/api/
bot_key = "bot key"
chat_id = chat_id
limit = 37152 #current bitcoin price 
time_interval = 10 #time per minute


#coin market cap Api code
def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    
    parameters = {
        'start':'1',
        'limit':'2',
        'convert':'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }

    response = requests.get(url, headers=headers,params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price

#link your program with your telegram chatbot
def send_update(chat_id, msg):    
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)

#main function and messages
def main():
    while True:
        price = get_price()
        print(price)
        if price < limit:
            send_update(chat_id, f"The bitcoin price lower than your limit: {price} and your limit was :{limit}")    
        else:
           send_update(chat_id, f"The bitcoin price is higher than your limit: {price} and your limit was :{limit}")    
        time.sleep(time_interval)

main()
