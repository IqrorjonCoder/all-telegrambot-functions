from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Sticker


def sticker(update, context):
    update.message.reply_text(f"your sticker data : \n\n\n{update.message.sticker}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', sticker))
    dispatcher.add_handler(MessageHandler(Filters.sticker, sticker))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
#
# data = {'type': 'regular',
#         'width': 512,
#         'is_video': False,
#         'file_unique_id': 'AgADhgADS0IiEQ',
#         'emoji': '😡',
#         'file_id': 'CAACAgIAAxkBAAIY3WN-RrIjjHwnj9Eflcdg-E7wSKFmAAKGAANLQiIR5UexTatOYDorBA',
#         'thumb': {'width': 128,
#                   'file_unique_id': 'AQADhgADS0IiEXI',
#                   'file_id': 'AAMCAgADGQEAAhjdY35GsiOMfCeP0R-Vx2D4TvBIoWYAAoYAA0tCIhHlR7FNq05gOgEAB20AAysE',
#                   'height': 128,
#                   'file_size': 4506},
#         'height': 512,
#         'set_name': 'Animatedstiker2',
#         'is_animated': True,
#         'file_size': 57136}
