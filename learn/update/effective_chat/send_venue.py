from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_venue(update, context):
    update.effective_chat.send_venue(latitude=41.303609 ,
                                     longitude=69.245264,
                                     title="this is title text",
                                     address="this is address text")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_venue))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
