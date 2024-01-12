import telebot.custom_filters

from init_bot import bot
from handlers import register_handlers
if __name__ == "__main__":
    register_handlers()
    bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))
    print("ok")
    bot.infinity_polling()
