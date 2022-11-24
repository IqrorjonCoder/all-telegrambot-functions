from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def voice(update, context):
    update.message.reply_text(f"voice is :\n\n{update.message.voice}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.voice, voice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
