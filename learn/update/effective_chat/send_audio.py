from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_audio(update, context):
    update.message.reply_text(f"send_audio : \n{update.effective_chat.send_audio(audio=open('/Users/student/PycharmProjects/iqrorjoncoder/base/mp3_example.mp3', 'rb'))}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_audio))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
