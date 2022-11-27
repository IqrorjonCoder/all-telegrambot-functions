from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_video(update, context):
    update.effective_chat.send_video(video=open("/Users/student/PycharmProjects/iqrorjoncoder/base/example_video.mp4", 'rb'),
                                     caption="this is an example video")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_video))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
