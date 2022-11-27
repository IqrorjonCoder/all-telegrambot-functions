from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def type(update, context):

    x = update.effective_chat.type
    update.message.reply_text(f"type : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', type))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
