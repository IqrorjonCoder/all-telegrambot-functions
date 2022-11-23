from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def reply_video(update, context):
    update.message.reply_text("hello ...")
    update.message.reply_video(video=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/example_video.mp4", 'rb'),
                               caption="this is simple exmaple video",
                               quote=True)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_video))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

