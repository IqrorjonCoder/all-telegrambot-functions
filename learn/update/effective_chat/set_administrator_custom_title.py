from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def set_administrator_custom_title(update, context):
    print(update.effective_user.id)
    update.message.reply_text(f"""hello ... {update.effective_chat.set_administrator_custom_title(user_id=1397003436, custom_title="Adminkaa")}""")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_administrator_custom_title))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
