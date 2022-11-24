from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def voice_chat_scheduled(update, context):
    update.message.reply_text(f"voice_chat_scheduled :\n\n{update.message.voice_chat_scheduled}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.voice_chat_scheduled, voice_chat_scheduled))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
