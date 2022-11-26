from telegram.ext import Updater, CommandHandler


def decline_join_request(update, context):
    update.message.reply_text("salom ...")
    update.effective_user.decline_join_request(chat_id=update.message.chat_id)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', decline_join_request))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()