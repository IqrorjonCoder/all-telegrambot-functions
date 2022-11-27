from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def title(update, context):

    x = update.effective_chat.title
    update.message.reply_text(f"title : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', title))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
