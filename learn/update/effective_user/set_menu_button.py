from telegram.ext import Updater, CommandHandler
from telegram import MenuButton


def set_menu_button(update, context):

    update.effective_user.set_menu_button(menu_button=MenuButton.DEFAULT)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_menu_button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
