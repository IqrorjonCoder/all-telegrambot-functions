from telegram.ext import Updater, CommandHandler
from telegram import InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo


def send_media_group(update, context):
    update.message.reply_text("salom ...")
    update.effective_user.send_media_group(media=[
        InputMediaAudio(media=open('/Users/student/PycharmProjects/iqrorjoncoder/base/mp3_example.mp3', 'rb'), caption="exampple audio 1"),
        InputMediaAudio(media=open('/Users/student/PycharmProjects/iqrorjoncoder/base/mp3_example.mp3', 'rb'), caption="exampple audio 2"),
        InputMediaAudio(media=open('/Users/student/PycharmProjects/iqrorjoncoder/base/mp3_example.mp3', 'rb'), caption="exampple audio 3"),
        # InputMediaDocument(media=open('/Users/student/PycharmProjects/iqrorjoncoder/base/example.py', 'rb'), caption="exampple document"),
        # InputMediaPhoto(media=open('/Users/student/PycharmProjects/iqrorjoncoder/base/AQADccIxGxCQoUsB.jpg', 'rb'), caption="exampple photo"),
        # InputMediaVideo(media=open('/Users/student/PycharmProjects/iqrorjoncoder/base/example_video.mp4', 'rb'), caption="exampple video"),
    ])



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_media_group))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()