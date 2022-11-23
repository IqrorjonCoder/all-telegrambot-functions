from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def to_json(update, context):
    print(update.message.to_json())
    update.message.reply_text(f"to_json is :  \n\n{update.message.to_json()}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, to_json))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

