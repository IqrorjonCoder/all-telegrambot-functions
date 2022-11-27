from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import MenuButton


def set_menu_button(update, context):
    update.message.reply_text(f"""hello ... {update.effective_chat.set_menu_button(MenuButton.DEFAULT)}""")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_menu_button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
