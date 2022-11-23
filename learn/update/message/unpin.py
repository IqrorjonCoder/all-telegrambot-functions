from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def unpin(update, context):
    print(update.message.message_id) #6411
    context.bot.unpin_chat_message(chat_id=update.message.chat_id,
                                   message_id=6411)
    update.message.reply_text("okok")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, unpin))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

