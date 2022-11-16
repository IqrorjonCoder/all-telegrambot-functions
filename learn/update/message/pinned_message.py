from telegram.ext import Updater, MessageHandler, Filters
from telegram import MessageEntity


def pinned_message(update, context):
    update.message.reply_text(f"{update.message.pinned_message}")
    update.message.reply_text("salom ...")


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.pinned_message, pinned_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()