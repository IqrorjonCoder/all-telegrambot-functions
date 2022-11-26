from telegram.ext import Updater, CommandHandler


def send_audio(update, context):
    update.message.reply_text("salom ...")
    update.effective_user.send_audio(audio=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/mp3_example.mp3", 'rb'),
                                         caption="this is an example audio!")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_audio))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()