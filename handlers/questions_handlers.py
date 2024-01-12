import telebot
from telebot.handler_backends import StatesGroup, State
from init_bot import bot


class Questions(StatesGroup):
    start_dialog = State()
    question2 = State()


@bot.message_handler(commands=["game_for_me"])
def test_start(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Самое главное, что ты должен запомнить: ")
    bot.send_message(message.chat.id, "У тебя есть пять яйц.")
    bot.send_message(message.chat.id, "Ты должен донести их до своего дома.")
    bot.send_message(message.chat.id, "Как я могу к тебе обращаться?")
    bot.set_state(message.chat.id, state=Questions.start_dialog)


@bot.message_handler(state=Questions.start_dialog)
def correct_answer(message: telebot.types.Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["user_name"] = message.text
    bot.send_message(message.chat.id, "Привет "+data["user_name"])


@bot.message_handler(state=Questions.start_dialog, func=lambda message: isinstance(message.text, str))
def answer(message: telebot.types.Message):
    print("str")
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #     data["user_name"] = message.text



