from telegram.ext import Updater, CommandHandler
from telegram import ChatAction


def send_contact(update, context):
    update.message.reply_text("salom ...")
    update.effective_user.send_contact(phone_number="+998 90 360 52 93",
                                       first_name="ex firstname",
                                       last_name="ex lastname")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_contact))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()