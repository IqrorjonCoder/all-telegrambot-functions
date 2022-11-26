from telegram.ext import Updater, CommandHandler


def added_to_attachment_menu(update, context):
    update.message.reply_text("salom ...")
    print(update.effective_user)
    print(update.effective_user.added_to_attachment_menu)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', added_to_attachment_menu))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()