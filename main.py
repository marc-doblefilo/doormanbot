import os
from decouple import config
import telebot
from telebot import types
import functions

TELEGRAM_TOKEN = config('API')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
wait_time = 10

@bot.message_handler(commands=['info'])
def info_message(message):
    info = "Good morning Sir or Madam, my name is DoormanBot. My creator is @markisafourletterword. I was created to be used by Aula Software Libre."
    bot.send_message(message.chat.id, info)

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def verify_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    captcha = types.InlineKeyboardButton("I'm not a robot", callback_data=reply)
    markup = types.InlineKeyboardMarkup(captcha)
    bot.send_message(chat_id, "Verify you're not a robot", reply_markup=markup)
    functions.stop_countdown = False
    if(functions.countdown(wait_time) == True):
        bot.send_message(chat_id, "You're a robot!")

def reply(message):
    functions.stop_countdown = True
    print("He's not a robot")



bot.polling()
