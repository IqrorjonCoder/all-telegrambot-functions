from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Animation


def getFile(update, context):
    print(update.message.animation)
    # anim = Animation(update.message.animation)
    animation = context.bot.getFile(update.message.animation)
    # animation.download()
    print(animation)


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.animation, getFile))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()