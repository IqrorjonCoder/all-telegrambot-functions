from telegram.ext import Updater, CommandHandler


def can_read_all_group_messages(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"{update.effective_user.can_read_all_group_messages}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', can_read_all_group_messages))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()