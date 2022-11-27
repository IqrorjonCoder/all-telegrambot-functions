from telegram.ext import Updater, CommandHandler


def supports_inline_queries(update, context):

    update.message.reply_text(f"{update.effective_user.supports_inline_queries}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', supports_inline_queries))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
