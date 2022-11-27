from telegram.ext import Updater, CommandHandler


def send_venue(update, context):

    update.effective_user.send_venue(latitude=41.311126,
                                     longitude=69.279824,
                                     address="Tashkent City",
                                     title="this is an example venue")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_venue))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
