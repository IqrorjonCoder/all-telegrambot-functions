from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def invite_link(update, context):
    x = update.effective_chat.invite_link
    update.message.reply_text(f"invite_link : \n{x}")
    print(x)


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', invite_link))
    dispatcher.add_handler(MessageHandler(Filters.all, invite_link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()