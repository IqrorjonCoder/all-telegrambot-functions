from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def video_chat_scheduled(update, context):

    update.message.reply_text(f"scheduled!!!")
    update.message.reply_text(f"video_chat_scheduled is : {update.message.video_chat_scheduled}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.video_chat_scheduled, video_chat_scheduled))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

