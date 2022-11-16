from telegram.ext import Updater, Filters, MessageHandler, CommandHandler


def reply_copy(update, context):
    update.message.reply_copy(from_chat_id="-1001609283019",
                              message_id=702,
                              ) #-1001609283019 #753


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_copy))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()