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

@bot.message_handler(commands=['help'])
def verify_user(message):
    id_newuser = message.chat.id
    print(id_newuser)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, selective=True)
    Verify_Button = types.KeyboardButton("I'm not a robot.")
    markup.add(Verify_Button)
    sent = bot.send_message(id_newuser, "Verify you're not a robot", reply_markup=markup)
    bot.register_next_step_handler(sent, reply)
    functions.stop_countdown = False
    if(functions.countdown(wait_time) == True):
        bot.send_message(id_newuser, "You're a robot!")

def reply(message):
    functions.stop_countdown = True
    bot.send_message(message.chat.id, "You're not a robot")



bot.polling()
