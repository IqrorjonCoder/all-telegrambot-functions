from telegram.ext import Updater, CommandHandler


def answer_pre_checkout_query(update, context):
    update.message.reply_text("salom ...")
    context.bot.answer_pre_checkout_query()


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', answer_pre_checkout_query))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()