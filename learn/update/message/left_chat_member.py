from telegram.ext import Updater, CommandHandler
from telegram import Invoice, LabeledPrice


def left_chat_member(update, context):
    update.message.reply_text("salom ...")
    print(update.message.left_chat_member)



def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', left_chat_member))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()