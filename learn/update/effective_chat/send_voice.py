from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_voice(update, context):
    update.effective_chat.send_voice(voice=open("/Users/student/PycharmProjects/iqrorjoncoder/base/example_voice.ogg", 'rb'))


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_voice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
