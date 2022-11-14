from telegram.ext import Updater, MessageHandler, Filters


def document(update, context):
    update.message.reply_text(f"you file : \n\n {update.message.document}")
    print(update.message.document)


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.document, document))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
