from telegram.ext import Updater, CommandHandler


def copy_message(update, context):
    update.effective_chat.copy_message(chat_id=update.message.chat_id,
                                       message_id=update.message.message_id-1)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', copy_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()