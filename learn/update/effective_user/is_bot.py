from telegram.ext import Updater, CommandHandler


def is_bot(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"{update.effective_user.is_bot}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', is_bot))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()