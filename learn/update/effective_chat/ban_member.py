from telegram.ext import Updater, CommandHandler


def ban_member(update, context):
    update.message.reply_text(f"members banned : {update.effective_chat.ban_member(user_id=update.message.from_user.id)}")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', ban_member))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()