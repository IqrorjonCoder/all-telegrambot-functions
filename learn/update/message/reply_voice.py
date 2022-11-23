from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Voice


def reply_voice(update, context):
    simple_voice = Voice(file_id="AwACAgIAAxkBAAIYzmN-OS0k8vTBVsRYuJRdLRSvUzkXAALVIAACL5P5S-5CVoXSezC7KwQ",
                         file_unique_id="AgAD1SAAAi-T-Us",
                         duration=100)
    # 1
    update.message.reply_voice(voice=simple_voice)

    # 2
    update.message.reply_voice(voice=open("C:/Users/student.ASTRUM-DOMAIN/PycharmProjects/minimi_bot/base/example_voice.ogg", 'rb'),
                               caption="this is simple example voice")

def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_voice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()


# {'duration': 2, 'file_size': 15906, 'file_id': 'AwACAgIAAxkBAAIYzmN-OS0k8vTBVsRYuJRdLRSvUzkXAALVIAACL5P5S-5CVoXSezC7KwQ', 'mime_type': 'audio/ogg', 'file_unique_id': 'AgAD1SAAAi-T-Us'}


