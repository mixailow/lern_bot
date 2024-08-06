
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

import settings


logging.basicConfig(filename="bot.log", level=logging.INFO)

def greet_user(update, context):
    print("вызов кнопки /start")
    update.message.reply_text("circle - обсёркл")

def talk_to_me(update, context):
    update.message.text
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater("settings.APY_KEY", use_context=True)

    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(filters.text, talk_to_me))

    logging.info("бот запущен")

    mybot.start_polling()
    mybot.idle()

if __name__== "__main__":
    main()