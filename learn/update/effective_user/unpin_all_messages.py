from telegram.ext import Updater, CommandHandler


def unpin_all_messages(update, context):

    update.message.reply_text(f"unpin all messages : {update.effective_user.unpin_all_messages()}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unpin_all_messages))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
