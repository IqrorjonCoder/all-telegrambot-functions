from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Sticker


def send_sticker(update, context):
    # update.effective_user.send_sticker(sticker=Sticker(file_id="CAACAgIAAxkBAAIaRGOC-Glj_JEPjS98Mp2ZO4PMHG9RAAJ3KAACU2IZSH0tHeeYIZeRKwQ",
    #                                                    file_unique_id="AQADdygAAlNiGUhy",
    #                                                    width=128,
    #                                                    height=126,
    #                                                    is_animated=False,
    #                                                    is_video=False,
    #                                                    type="redefined-builtin"))
    update.effective_user.send_sticker(sticker=open("/Users/student/PycharmProjects/iqrorjoncoder/base/example_stickerfile.tgs", 'rb'))


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_sticker))
    # dispatcher.add_handler(MessageHandler(Filters.sticker, send_sticker))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

    # {'is_video': False, 'type': 'regular',
    #  'file_id': 'CAACAgIAAxkBAAIaRGOC-Glj_JEPjS98Mp2ZO4PMHG9RAAJ3KAACU2IZSH0tHeeYIZeRKwQ', 'height': 512,
    #  'is_animated': True,
    #  'thumb': {'file_id': 'AAMCAgADGQEAAhpEY4L4aWP8kQ-NL3wynZk7g8wcb1EAAncoAAJTYhlIfS0d55ghl5EBAAdtAAMrBA',
    #            'height': 128, 'file_size': 126, 'width': 128, 'file_unique_id': 'AQADdygAAlNiGUhy'}, 'file_size': 7443,
    #  'width': 512, 'file_unique_id': 'AgADdygAAlNiGUg'}
