import telebot

from init_bot import bot



@bot.message_handler(commands=["start"])
def start_bot(message: telebot.types.Message):
    bot.reply_to(message, "Hello my dear friend")
    bot.send_message(message.chat.id, "Commands available:\n /books_for_me\n /movies")


@bot.message_handler(commands=["books_for_me"])
def books_call(message: telebot.types.Message):
    books_markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard= True)
    books_markup.add(telebot.types.KeyboardButton("Фентези"))
    books_markup.add(telebot.types.KeyboardButton("Классика"))
    books_markup.add(telebot.types.KeyboardButton("Фантанстика"))
    bot.reply_to(message, "Какой жанр книг вы предпочитаете?", reply_markup=books_markup)

    # with open("itoms.txt", "r") as file:
    #     books = file.read().split("\n")
    #     books = random.choice(books)
    # bot.send_message(message.chat.id, books)


@bot.message_handler(func= lambda message : message == "Классика")
def send_classic(message: telebot.types.Message):
    with open("itoms.txt") as file:
        books = file.read().split("\n")
        books = random.choice(books)
    bot.send_message(message.chat.id, books)


@bot.message_handler(commands=["movies"])
def start_bot(message: telebot.types.Message):
    movies_in_markup = telebot.util.quick_markup(
        {"Атака титанов": {"url": "https://ataka-titanov.com/"}

          # "Слово пердуна": {"callback_data": "smart"}
        })
    bot.reply_to(message, "вот ссылки", reply_markup= movies_in_markup)



# @bot.message_handler(func =)