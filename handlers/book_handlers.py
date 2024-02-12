import telebot

from init_bot import bot
import random


@bot.message_handler(commands=["books_for_me"])
def books_call(message: telebot.types.Message):
    books_markup = telebot.util.quick_markup({
        "Классика": {"callback_data": "classic"},
        "Фентези": {"callback_data": "fentezi"},
        "Детективы":{"callback_data": "detective"}

    })
    bot.reply_to(message, "Выберите жанр", reply_markup=books_markup)
    # books_markup = telebot.types.InlineKeyboardMarkup()
    # books_markup.add(telebot.types.InlineKeyboardButton("Фентези", url= "kwksjw"))
    # books_markup.add(telebot.types.InlineKeyboardButton("Классика", callback_data="classic"))
    # books_markup.add(telebot.types.InlineKeyboardButton("Фантанстика", url="swhgs"))
    # bot.reply_to(message, "Какой жанр книг вы предпочитаете?", reply_markup=books_markup)


@bot.callback_query_handler(func= lambda callback: callback.data == "classic")
def send_classic(callback: telebot.types.CallbackQuery):
    with open("classic.txt", encoding="utf") as file:
        books = file.read().split("\n")
        books = random.choice(books)
    bot.send_message(callback.message.chat.id, books)


@bot.callback_query_handler(func=lambda callback: callback.data == "fentezi")
def send_fentezi(callback: telebot.types.CallbackQuery):
    with open("fentezi.txt", encoding="utf") as file:
        f_books = file.read().split("\n")
        f_books = random.choice(f_books)
    bot.send_message(callback.message.chat.id, f_books)


@bot.callback_query_handler(func=lambda callback: callback.data == "detective")
def send_detective(callback: telebot.types.CallbackQuery):
    with open("detective.txt", encoding="utf") as file:
        books = file.read().split("\n")
        books = random.choice(books)
    bot.send_message(callback.message.chat.id, books)