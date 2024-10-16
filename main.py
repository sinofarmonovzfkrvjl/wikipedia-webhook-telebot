from telebot import TeleBot, types
import logging
import wikipedia
from deep_translator import GoogleTranslator

API_TOKEN = "7257169762:AAFKf38iie-TiO3MfgKCX6bjHgOgPkWYZNA"

bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message: types.Message):
    bot.send_message(message.chat.id, GoogleTranslator(target=message.from_user.language_code).translate(f"Salom {message.from_user.full_name}"))

@bot.message_handler(func=lambda message: message.text.startswith("/"))
def change_lang(message: types.Message):
    wikipedia.set_lang(message.text[1:])
    bot.send_message(message.chat.id, GoogleTranslator(target=message.from_user.language_code).translate("Til o'zgartirildi") + " to " + message.text[1:])

@bot.message_handler()
def echo(message: types.Message):
    try:
        bot.send_message(message.chat.id, wikipedia.summary(message.text))
    except:
        bot.send_message(message.chat.id, GoogleTranslator(target=message.from_user.language_code).translate("Bu mavzuga oid maqola topaolmadim"))
