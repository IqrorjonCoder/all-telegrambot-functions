from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction


def send_action(update, context):
    update.effective_chat.send_action(action=ChatAction.RECORD_AUDIO)
    update.message.reply_text(f"send_action : \n{12}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_action))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
