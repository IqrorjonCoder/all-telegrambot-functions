from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_document(update, context):
    update.message.reply_text(f"send_document : \n{update.effective_chat.send_document(document=open('/Users/student/PycharmProjects/iqrorjoncoder/base/example.py', 'rb'))}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_document))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
