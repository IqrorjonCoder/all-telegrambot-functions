from telegram.ext import Updater, CommandHandler
import datetime


def create_invite_link(update, context):
    update.message.reply_text(f"invite link : \n{update.effective_chat.create_invite_link(expire_date=datetime.datetime.now())}")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', create_invite_link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()