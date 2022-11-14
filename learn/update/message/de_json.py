from telegram.ext import CommandHandler, Updater


def de_json(update, context):
    update.message.reply_text(f"{update.message.to_json()}")
    print(update.message.to_json())


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', de_json))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
