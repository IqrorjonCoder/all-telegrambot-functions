from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatPermissions


def photo(update, context):

    update.message.reply_text(f"photo : \n{update.effective_chat.photo}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', photo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
