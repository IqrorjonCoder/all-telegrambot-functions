from telegram.ext import Updater, CommandHandler


def chat(update, context):
    update.message.reply_text(f"id : {update.message.chat['id']}\n"
                              f"title : {update.message.chat['title']}\n"
                              f"username : {update.message.chat['username']}")


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()