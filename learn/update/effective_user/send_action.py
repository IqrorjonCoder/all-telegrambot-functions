from telegram.ext import Updater, CommandHandler
from telegram import ChatAction


def send_action(update, context):
    update.message.reply_text("salom ...")
    update.effective_user.send_chat_action(action=ChatAction.TYPING)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_action))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()