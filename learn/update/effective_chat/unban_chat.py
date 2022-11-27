from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def unban_chat(update, context):

    x = update.effective_chat.unban_chat(chat_id=update.effective_chat.id)
    update.message.reply_text(f"unban_chat : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unban_chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
