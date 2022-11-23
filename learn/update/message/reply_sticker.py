from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def reply_sticker(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_sticker(sticker=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/example_stickerfile.tgs", 'rb'))


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_sticker))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()