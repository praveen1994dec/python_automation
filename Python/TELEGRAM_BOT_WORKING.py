#pip install python-telegram-bot
import telegram 

import requests

import json

from telegram.bot import Bot 

bot = telegram.Bot(token='5923635818:AAFsDcVUx60nuzx6wHiDUJzst5F0xbwpdB0') #Replace TOKEN with your token string

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater(token='5923635818:AAFsDcVUx60nuzx6wHiDUJzst5F0xbwpdB0', use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher


#hello world response
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, This is a telegram bot')

#rest api hit and get data
def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200): #Everything went okay, we have the data
        data = response.json()
        print(data['Global'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=data['Global'])
    else: #something went wrong
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")

corona_summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)


#If hello comes to bot it will redirect to hello method

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)




def electronic(update, context):
    response = requests.get('https://dummyjson.com/products/search?q=Laptop')
    if(response.status_code==200): #Everything went okay, we have the data
        data = response.json()
        print(data['products'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=data['products'])
    else: #something went wrong
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")

electronic_summary_handler = CommandHandler('electronic', electronic)
dispatcher.add_handler(electronic_summary_handler)




# For Commands 
def fnc1(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to the www.praveensingampalli.com ",
        )
start_value2=CommandHandler('start', fnc1)
dispatcher.add_handler (start_value2)

#adding more Command
def fnc2(update, context):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="tutorial link: wwww.youtube.com/praveensingampalli ",
        )
start_value=CommandHandler('youtube', fnc2)
dispatcher.add_handler (start_value)


updater.start_polling()