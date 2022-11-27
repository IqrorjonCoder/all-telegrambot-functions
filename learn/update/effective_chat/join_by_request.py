from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def join_by_request(update, context):
    x = update.effective_chat.join_by_request
    update.message.reply_text(f"join_by_request : \n{x}")
    print(x)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', join_by_request))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()