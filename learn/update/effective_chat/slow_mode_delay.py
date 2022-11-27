from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def slow_mode_delay(update, context):

    x = update.effective_chat.slow_mode_delay
    update.message.reply_text(f"slow_mode_delay : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', slow_mode_delay))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
