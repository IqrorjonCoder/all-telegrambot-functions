import kwargs as kwargs
from telegram.ext import Updater, MessageHandler, Filters
from telegram import MessageAutoDeleteTimerChanged


def message_auto_delete_timer_changed(update, context):
    update.message.message_auto_delete_timer_changed(MessageAutoDeleteTimerChanged(message_auto_delete_time=12))


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, message_auto_delete_timer_changed))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()