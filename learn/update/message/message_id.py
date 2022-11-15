from telegram.ext import Updater, MessageHandler, Filters


def message_id(update, context):
    update.message.reply_text(f"your message id : {update.message.message_id}")


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, message_id))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()