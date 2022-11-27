from telegram.ext import Updater, CommandHandler


def full_name(update, context):
    update.message.reply_text(f"""full_name : \n{update.effective_chat.full_name}""")





def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', full_name))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()