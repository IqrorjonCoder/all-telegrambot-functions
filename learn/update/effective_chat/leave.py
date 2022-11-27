from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def leave(update, context):
    x = update.effective_chat.leave()
    update.message.reply_text(f"leave : \n{x}")
    print(x)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', leave))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()