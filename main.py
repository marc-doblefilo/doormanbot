import os
from decouple import config
import telebot

TELEGRAM_TOKEN = config('API')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['info'])
def send_message(message):
    bot.reply_to(message, "HELLO")


bot.polling()