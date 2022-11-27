from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def link(update, context):

    update.message.reply_text(f"link : \n{update.effective_chat.link}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()