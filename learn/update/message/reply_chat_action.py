from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import ChatAction


def reply_chat_action(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_chat_action(action=ChatAction.FIND_LOCATION)


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_chat_action))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()