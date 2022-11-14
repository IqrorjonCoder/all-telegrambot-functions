from telegram.ext import Updater, CommandHandler


def delete_chat_photo(update, context):
    update.message.reply_text("salom ...")
    print(update.message.delete_chat_photo)
    context.bot.delete_chat_photo(chat_id="-1001609283019")


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', delete_chat_photo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()