import telebot
from telebot.handler_backends import StatesGroup, State
from init_bot import bot


class Questions(StatesGroup):
    start_dialog = State()
    question2 = State()


def str_check(message: telebot.types.Message):
    text = message.text
    for i in text:
        if i.isdigit():
            return False
    else:
        return True


@bot.message_handler(commands=["game_for_me"])
def test_start(message: telebot.types.Message):
    # bot.send_photo(message.chat.id)
    bot.send_message(message.chat.id, "Самое главное, что ты должен запомнить: ")
    bot.send_message(message.chat.id, "У тебя есть пять ракушек.")
    bot.send_message(message.chat.id, "Ты должен донести их до своего дома.")
    bot.send_message(message.chat.id, "Как я могу к тебе обращаться?")
    bot.set_state(message.chat.id, state=Questions.start_dialog)


@bot.message_handler(state=Questions.start_dialog)
def name_answer(message: telebot.types.Message):
    if str_check(message):
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["user_name"] = message.text
            with open("name.txt", "w", encoding="utf-8") as file:
                file.write(data["user_name"])
        bot.send_message(message.chat.id, "привет "+data["user_name"])
        bot.set_state(message.chat.id, state=Questions.question2)
    else:
        bot.send_message(message.chat.id, "пожалуйста, введи своё имя буквами")


@bot.message_handler(state=Questions.question2)
def first_question(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Ты живёшь в очень странном и одновременно красивом месте. "
                                      "Твой маленький мир полностью состоит из висящих в воздухе островов, соединённых верёвочными мостами.")
