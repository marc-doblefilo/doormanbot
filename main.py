import os
from decouple import config
import telebot
from telebot import types

TELEGRAM_TOKEN = config('API')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['info'])
def verify_user(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    Verify_Button = types.KeyboardButton("I'm not a robot.")
    markup.add(Verify_Button)
    bot.send_message(message.chat.id, "Verify you're not a robot", reply_markup=markup)

bot.polling()
