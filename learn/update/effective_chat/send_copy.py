from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def send_copy(update, context):
    update.message.reply_text(f"send_copy : \n{update.effective_chat.send_copy(from_chat_id=update.effective_chat.id,message_id=update.message.message_id-1)}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_copy))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
