import telebot
from init_bot import bot


@bot.message_handler(commands=["movies"])
def start_bot(message: telebot.types.Message):
    movies_in_markup = telebot.util.quick_markup({
        "Атака титанов": {"url": "https://ataka-titanov.com/"},
        "Мандалорец": {"url": "https://13lordserial.online/3870-mandalorec-1-3-sezon-s20.html", "callback_data": "smart"}

    })
    bot.reply_to(message, "вот ссылки", reply_markup=movies_in_markup)


@bot.callback_query_handler(func=lambda callback: callback.data == "smart")
def mandolor_wh(callback: telebot.types.CallbackQuery):
    pass