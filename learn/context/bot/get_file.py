from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Animation


def get_file(update, context):
    print(update.message.animation)
    # anim = Animation(update.message.animation)
    animation = context.bot.get_file(update.message.animation)
    # animation.download()
    print(animation)


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', get_file))
    dispatcher.add_handler(MessageHandler(Filters.animation, get_file))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()