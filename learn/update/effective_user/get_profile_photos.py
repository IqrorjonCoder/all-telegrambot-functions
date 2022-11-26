from telegram.ext import Updater, CommandHandler


def get_profile_photos(update, context):
    update.message.reply_text("salom ...")
    print(update.effective_user.get_profile_photos())


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_profile_photos))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()