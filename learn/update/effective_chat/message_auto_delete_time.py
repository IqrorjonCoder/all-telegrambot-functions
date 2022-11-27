from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def message_auto_delete_time(update, context):
    x = update.effective_chat.message_auto_delete_time
    update.message.reply_text(f"message_auto_delete_time : \n{x}")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', message_auto_delete_time))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()