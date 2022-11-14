from telegram.ext import CommandHandler, Updater


def copy(update, context):
    print(update.message.message_id)
    print(update.message.copy(chat_id=update.message.chat_id))



def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', copy))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
