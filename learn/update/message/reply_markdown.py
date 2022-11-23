from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def reply_markdown(update, context):
    update.message.reply_markdown("*bold* is _italic_")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_markdown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()