from telegram.ext import Updater, CommandHandler
from telegram import Invoice, LabeledPrice


def is_automatic_forward(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"automatic forward is : {update.message.is_automatic_forward}")



def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', is_automatic_forward))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()