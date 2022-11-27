from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def unpin_all_messages(update, context):

    x = update.effective_chat.unpin_all_messages()
    update.message.reply_text(f"unpin_all_messages : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unpin_all_messages))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
