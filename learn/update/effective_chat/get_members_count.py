from telegram.ext import Updater, CommandHandler


def get_members_count(update, context):
    x = update.effective_chat.get_members_count()
    update.message.reply_text(f"get member : \n{x}")
    print(x)





def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_members_count))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()