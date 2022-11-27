from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def to_dict(update, context):

    x = update.effective_chat.to_dict()
    update.message.reply_text(f"to_dict : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', to_dict))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
