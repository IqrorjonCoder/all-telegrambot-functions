from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction


def send_animation(update, context):
    update.message.reply_text(f"send_animation : \n{update.effective_chat.send_animation(animation=open('/Users/student/PycharmProjects/iqrorjoncoder/base/gif_example.mp4', 'rb'))}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_animation))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
