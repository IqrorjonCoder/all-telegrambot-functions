from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def venue(update, context):
    update.message.reply_text(f"vennue is : \n\n{update.message.venue}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.venue, venue))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

