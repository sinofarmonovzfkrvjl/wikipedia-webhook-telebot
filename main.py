from telebot import TeleBot, types
import wikipedia
from deep_translator import GoogleTranslator

API_TOKEN = "7257169762:AAEHq_ki3WaO3L09UGcHx7mPUIb4eVwoaiA"

bot = TeleBot(API_TOKEN)

@bot.message_handler(commands=["start"])
def start(message: types.Message):
    bot.send_message(message.chat.id, GoogleTranslator(target=message.from_user.language_code).translate(f"Salom {message.from_user.full_name} men wikipedia botman"))

@bot.message_handler(commands=['uz'])
def uz(message: types.Message):
    wikipedia.set_lang('uz')
    bot.send_message(message.chat.id, "Til o'zgartirildi")

@bot.message_handler(commands=['ru'])
def ru(message: types.Message):
    wikipedia.set_lang('ru')
    bot.send_message(message.chat.id, "Язык изменен")

@bot.message_handler(commands=['en'])
def en(message: types.Message):
    wikipedia.set_lang('en')
    bot.send_message(message.chat.id, "Language changed")

@bot.message_handler()
def echo(message: types.Message):
    try:
        bot.send_message(message.chat.id, wikipedia.summary(message.text))
    except:
        bot.send_message(message.chat.id, GoogleTranslator(target=message.from_user.language_code).translate("Bu mavzuga oid maqola topaolmadim"))


if __name__ == "__main__":
    bot.delete_webhook()
    bot.polling()
