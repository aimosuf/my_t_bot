import telebot
from init_bot import bot


@bot.message_handler(commands=["movies"])
def start_bot(message: telebot.types.Message):
    movies_in_markup = telebot.util.quick_markup({
        "Атака титанов": {"url": "https://ataka-titanov.com/"},
         "Слово пацана": {"callback_data": "smart"}

    })
    bot.reply_to(message, "вот ссылки", reply_markup=movies_in_markup)


@bot.callback_query_handler(func=lambda callback: callback.data == "smart")
def slovo_perdyna(callback: telebot.types.CallbackQuery):
    bot.send_message(callback.message.chat.id, "нет")