import datetime
from time import sleep

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def edit_date(update, context):
    print(update.message.message_id)
    print(update.message.edit_date)


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', edit_date))
    # dispatcher.add_handler(MessageHandler(Filters.animation, edit_date))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print('ishga tushdi ...')
    runner()