# With API
import requests
import telepot

print("Stock Price Notification")
inp_price = str(input("Which Stock you want to notify?\n"))

url = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+inp_price+"&apikey=KDOFGR4ZPP7FGIHR"
price = requests.get(url).json()
# print(price)

stock_price = price['Global Quote']['05. price']
print("Stock Price is ",stock_price,"$")
sendingMsg = "Stock Price of "+inp_price+" is "+stock_price+"$.";

token = '5769141027:AAEIMFDS3qevdDNrI4k5td6xH6OIo7Uvkfg'
reciever_id = 5129156347 #my telegram ID

bot = telepot.Bot(token)
bot.sendMessage(reciever_id,sendingMsg)
print("Message Succesfully Sent to your Telegram!")