from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def stop_live_location(update, context):
    # print(update.message.location)
    # print(update.message.message_id)

    update.message.stop_live_location(reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("salom", callback_data="salom")]]))

    context.bot.stop_message_live_location(chat_id=update.message.chat_id,
                                           message_id=6370,
                                           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("salom", callback_data="salom")]]))


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', stop_live_location))
    dispatcher.add_handler(MessageHandler(Filters.location, stop_live_location))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

# {'latitude': 41.303578, 'longitude': 69.289032} #6370