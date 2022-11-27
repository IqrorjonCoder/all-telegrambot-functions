from telegram.ext import Updater, CommandHandler


def has_protected_content(update, context):
    x = update.effective_chat.has_protected_content
    update.message.reply_text(f"has_protected_content : \n{x}")
    print(x)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', has_protected_content))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()