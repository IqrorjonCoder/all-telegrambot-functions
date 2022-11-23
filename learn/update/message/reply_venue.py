from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def reply_venue(update, context):
    update.message.reply_text("hello ...")
    update.message.reply_venue(latitude=41.303578,
                               longitude=69.289032,
                               address="Tashkent",
                               title="Tahskent city, Reformatuz company")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_venue))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

# {'latitude': 41.303578, 'longitude': 69.289032}