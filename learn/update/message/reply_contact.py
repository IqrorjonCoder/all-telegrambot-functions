from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Contact


def reply_contact(update, context):
    print(update.message.from_user)
    # 1
    update.message.reply_contact(phone_number="+998 90 360 52 93",
                                 first_name="iqrorjonc",
                                 last_name="islomovv")

    # 2
    update.message.reply_contact(contact=Contact(phone_number="+998 90 360 52 93",
                                                 first_name="iqrorjonc",
                                                 last_name="islomovv",
                                                 user_id=1035463819))

def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_contact))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()