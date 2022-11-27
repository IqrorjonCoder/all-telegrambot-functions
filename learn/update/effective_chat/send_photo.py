from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_photo(update, context):
    update.effective_chat.send_photo(photo=open('/Users/student/PycharmProjects/iqrorjoncoder/base/AQADccIxGxCQoUsB.jpg', 'rb'),
                                     caption="this is an exmaple picture")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_photo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
