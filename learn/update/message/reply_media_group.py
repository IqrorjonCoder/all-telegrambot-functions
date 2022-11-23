from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InputMediaDocument


def reply_media_group(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_media_group([
        InputMediaDocument(media=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/learn/update/message/reply_dice.py", 'rb'), caption="this is an example") for i in range(10)
    ])


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_media_group))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()