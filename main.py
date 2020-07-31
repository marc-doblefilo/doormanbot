import os
from decouple import config
import telebot
from telebot import types
import functions

TELEGRAM_TOKEN = config('API')

bot = telebot.TeleBot(TELEGRAM_TOKEN)
wait_time = 25

@bot.message_handler(commands=['info'])
def info_message(message):
    info = "Good morning Sir or Madam, my name is DoormanBot. My creator is @markisafourletterword. I was created to be used by Aula Software Libre."
    bot.send_message(message.chat.id, info)

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def verify_user(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    print(message.from_user.username + " entered " + message.chat.title)
    captcha = types.InlineKeyboardButton("I'm not a robot", callback_data="ok")
    markup = types.InlineKeyboardMarkup()
    markup.add(captcha)
    bot.send_message(chat_id, "Verify you're not a robot", reply_markup=markup)
    functions.stop_countdown = False
    if(functions.countdown(wait_time) == True):
        bot.kick_chat_member(chat_id, user_id)
        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if call.message:
        if call.data == "ok":
            functions.stop_countdown = True
            print("Is not a robot.")
            bot.delete_message(chat_id, message_id)


bot.polling()
