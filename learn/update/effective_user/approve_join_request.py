from telegram.ext import Updater, CommandHandler


def approve_join_request(update, context):
    update.message.reply_text("salom ...")
    print(update.message.chat_id)
    update.effective_user.approve_join_request(chat_id='-1001609283019')


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', approve_join_request))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()