from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def pinned_message(update, context):

    update.message.reply_text(f"pinned_message : \n{update.effective_chat.pinned_message}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', pinned_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
