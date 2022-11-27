from telegram.ext import Updater, CommandHandler


def username(update, context):

    update.message.reply_text(f"username : *{update.effective_user.username}*", parse_mode="Markdown")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', username))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
