from telegram.ext import Updater, CommandHandler


def ban_chat(update, context):
    update.message.reply_text(f"all members are admin : {123}")
    print(update.effective_chat.ban_chat(chat_id=update.message.chat_id))



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', ban_chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()