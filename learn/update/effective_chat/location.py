from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatLocation, Location


def location(update, context):

    update.message.reply_text(f"location : \n{update.effective_chat.location}")
    # update.message.reply_location(location=ChatLocation(location=Location(longitude=69.242220,
    #                                                                       latitude=41.326503),
    #                                                     address="tashkent city"))

def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', location))
    # dispatcher.add_handler(MessageHandler(Filters.location, location))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()