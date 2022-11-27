from telegram.ext import Updater, CommandHandler


def unpin_message(update, context):

    update.message.reply_text(f"unpin message : {update.effective_user.unpin_message(message_id=update.message.message_id-2)}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unpin_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
