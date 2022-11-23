from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


def reply_markup(update, context):
    # update.message.reply_markup(InlineKeyboardMarkup([[InlineKeyboardButton("one", callback_data="one")],
    #                                                   [InlineKeyboardButton("two", callback_data="two")]]))
    update.message.reply_text("salom", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("one", callback_data="one")],
                                                                          [InlineKeyboardButton("two", callback_data="two")]]))

    print(update.message.reply_markup)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', reply_markup))
    dispatcher.add_handler(MessageHandler(Filters.text, reply_markup))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()