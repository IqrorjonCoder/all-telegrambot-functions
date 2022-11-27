from telegram.ext import Updater, CommandHandler


def get_administrators(update, context):
    update.message.reply_text(f"""get_administrators : \n{[i.user.full_name for i in update.effective_chat.get_administrators()]}""")





def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_administrators))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()