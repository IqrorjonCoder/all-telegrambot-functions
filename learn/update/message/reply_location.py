from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Location, ReplyKeyboardMarkup, KeyboardButton


def reply_location(update, context):
    # update.message.reply_text("location", reply_markup=ReplyKeyboardMarkup([[KeyboardButton("location !!!", request_location=True)]], resize_keyboard=True))

    # {'latitude': 41.360154, 'longitude': 69.38129}

    # 1
    update.message.reply_location(latitude=41.360154,
                                  longitude=69.38129)

    # 2
    update.message.reply_location(location=Location(latitude=41.360154,
                                                    longitude=69.38129,
                                                    heading=1))


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(MessageHandler(Filters.location, reply_location))
    dispatcher.add_handler(CommandHandler('start', reply_location))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()