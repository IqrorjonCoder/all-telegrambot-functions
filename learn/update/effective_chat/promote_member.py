from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def promote_member(update, context):
    update.message.reply_text(f"promote_member : \n{update.effective_chat.promote_member(user_id=update.effective_user.id, can_promote_members=True)}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', promote_member))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
