from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InputMediaDocument


def send_media_group(update, context):
    update.effective_chat.send_media_group(media=[
        InputMediaDocument(media=open('/Users/student/PycharmProjects/iqrorjoncoder/learn/update/effective_chat/send_copy.py', 'rb'), caption="axample 1"),
        InputMediaDocument(media=open('/Users/student/PycharmProjects/iqrorjoncoder/learn/update/effective_chat/send_copy.py', 'rb'), caption="axample 2"),
        InputMediaDocument(media=open('/Users/student/PycharmProjects/iqrorjoncoder/learn/update/effective_chat/send_copy.py', 'rb'), caption="axample 3"),
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
