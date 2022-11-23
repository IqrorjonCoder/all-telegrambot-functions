from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def successful_payment(update, context):
    update.message.reply_text(f"your successful payment:  {update.message.successful_payment}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', successful_payment))
    dispatcher.add_handler(MessageHandler(Filters.successful_payment, successful_payment))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

