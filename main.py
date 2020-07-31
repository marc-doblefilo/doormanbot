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
    captcha_message = bot.send_message(chat_id, "@" + message.from_user.username + " verify you're not a robot", reply_markup=markup)
    message_id = captcha_message.message_id
    functions.stop_countdown = False
    if(functions.countdown(wait_time) == True):
        bot.delete_message(chat_id, message_id)
        if(bot.get_chat_member(chat_id, user_id).status != "creator" and bot.get_chat_member(chat_id, user_id).status != "administrator"):
            print(message.from_user.username + " who entered in " + message.chat.title + " didn't answered the captcha and was kicked.")
            bot.kick_chat_member(chat_id, user_id)
        else:
            print(message.from_user.username + " who entered in " + message.chat.title + " didn't answered the captcha but it's an admin.")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    if call.message:
        if call.data == "ok":
            functions.stop_countdown = True
            print(call.message.chat.title + " OK.")
            bot.delete_message(chat_id, message_id)


bot.polling()
