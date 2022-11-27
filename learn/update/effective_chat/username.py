from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def username(update, context):

    x = update.effective_chat.username
    update.message.reply_text(f"username : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', username))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
