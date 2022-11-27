from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_sticker(update, context):
    update.effective_chat.send_sticker(sticker=open('/Users/student/PycharmProjects/iqrorjoncoder/base/example_stickerfile.tgs', 'rb'))


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_sticker))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
