import telebot

from init_bot import bot


@bot.message_handler(func=lambda message: True)
def other_m(message: telebot.types.Message):
    bot.send_message(message.chat.id, "I dont understand")
