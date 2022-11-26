from telegram.ext import Updater, CommandHandler


def name(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"Come on my profile ! {update.effective_user.name}")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', name))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()