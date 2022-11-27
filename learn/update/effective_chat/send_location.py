from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_location(update, context):
    update.effective_chat.send_location(longitude=69.245264,
                                        latitude=41.303609)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_location))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
