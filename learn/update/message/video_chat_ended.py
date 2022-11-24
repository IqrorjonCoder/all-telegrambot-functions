from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def video_chat_ended(update, context):

    update.message.reply_text(f"ended!!!")
    update.message.reply_text(f"video_chat_ended is : {update.message.video_chat_ended}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.video_chat_ended, video_chat_ended))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

