from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def web_app_data(update, context):
    update.message.reply_text(f"web_app_data :\n\n{update.message.web_app_data}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.web_app_data, web_app_data))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
