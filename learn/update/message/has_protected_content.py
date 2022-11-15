from telegram.ext import Updater, CommandHandler


def has_protected_content(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"has protected content is : {update.message.has_protected_content}")



def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', has_protected_content))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()