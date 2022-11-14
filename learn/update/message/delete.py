from telegram.ext import Updater, CommandHandler


def delete(update, cntext):
    update.message.reply_text("salom ...")
    update.message.delete(timeout=100)


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', delete))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()