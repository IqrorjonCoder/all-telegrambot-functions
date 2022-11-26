from telegram.ext import Updater, CommandHandler


def first_name(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"{update.effective_user.first_name}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', first_name))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()