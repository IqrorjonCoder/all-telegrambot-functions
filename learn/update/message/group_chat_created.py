from telegram.ext import Updater, CommandHandler


def group_chat_created(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"group chat created is : {update.message.group_chat_created}")



def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', group_chat_created))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()