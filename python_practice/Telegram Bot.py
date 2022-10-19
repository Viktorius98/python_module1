import telebot

bot = telebot.TeleBot("TOKEN")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")

    bot.polling(none_stop=True)