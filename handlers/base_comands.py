import telebot

from init_bot import bot


@bot.message_handler(commands=["start"])
def start_bot(message: telebot.types.Message):
    text = message.from_user.full_name
    bot.reply_to(message, f"Привет {text}")
    bot.send_message(message.chat.id, "Commands available:\n /books_for_me\n /movies\n /game_for_me")



