from telegram.ext import Updater, CommandHandler


def pin_message(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"Come on my profile ! {123}")
    update.effective_user.pin_message(message_id=update.message.message_id-1)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', pin_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()