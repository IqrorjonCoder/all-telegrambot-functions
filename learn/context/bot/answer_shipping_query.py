from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def answer_shipping_query(update, context):
    print(dir(update.message.invoice))
    update.message.reply_text("salom ...")
    context.bot.answer_shipping_query(shipping_query_id=update.message.message_id,
                                      ok=False)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', answer_shipping_query))
    dispatcher.add_handler(MessageHandler(Filters.invoice, answer_shipping_query))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()