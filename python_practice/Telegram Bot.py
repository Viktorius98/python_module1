import telebot

TOKEN = "5716164818:AAEq0mi2V4irNlU4ldTgw55AaEgWvmFy0sk"

bot = telebot.TeleBot(TOKEN)

bot.polling(none_stop=True)