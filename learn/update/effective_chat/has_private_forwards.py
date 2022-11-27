from telegram.ext import Updater, CommandHandler


def has_private_forwards(update, context):
    x = update.effective_chat.has_private_forwards
    update.message.reply_text(f"has_private_forwards : \n{x}")
    print(x)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', has_private_forwards))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()