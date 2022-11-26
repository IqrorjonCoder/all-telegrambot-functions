from telegram.ext import Updater, CommandHandler


def send_document(update, context):
    update.message.reply_text("salom ...")
    update.effective_user.send_document(document=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/example.py", 'rb'))



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_document))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()