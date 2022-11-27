from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def linked_chat_id(update, context):

    update.message.reply_text(f"linked_chat_id : \n{update.effective_chat.linked_chat_id}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', linked_chat_id))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()