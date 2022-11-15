from telegram.ext import Updater, CommandHandler


def migrate_from_chat_id(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(update.message.migrate_from_chat_id)


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', migrate_from_chat_id))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()