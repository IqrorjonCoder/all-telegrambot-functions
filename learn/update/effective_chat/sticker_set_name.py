from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def sticker_set_name(update, context):

    x = update.effective_chat.sticker_set_name
    update.message.reply_text(f"sticker_set_name : \n{x}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sticker_set_name))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
