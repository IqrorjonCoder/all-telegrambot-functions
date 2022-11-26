from telegram.ext import Updater, CommandHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton


def get_menu_button(update, context):
    update.message.reply_text("salom ...", reply_markup=ReplyKeyboardMarkup([[KeyboardButton('salom')]]))
    print(update.effective_user.get_menu_button())


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_menu_button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()