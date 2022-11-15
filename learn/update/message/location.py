from telegram.ext import Updater, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup


def link(update, context):
    update.message.reply_text(f"location : \n{update.message.location}")


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.location, link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()