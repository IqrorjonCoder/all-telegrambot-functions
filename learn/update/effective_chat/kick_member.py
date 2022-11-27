from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def kick_member(update, context):
    x = update.effective_chat.kick_member(user_id=update.message.from_user.id)
    update.message.reply_text(f"kick_member : \n{x}")
    print(x)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', kick_member))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()