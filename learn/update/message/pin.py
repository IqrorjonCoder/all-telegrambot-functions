from telegram.ext import Updater, MessageHandler, Filters
from telegram import MessageEntity


def pin(update, context):
    update.message.pin()
    update.message.reply_text(f"your message pinned ... \n {update.message.text} ")


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, pin))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()