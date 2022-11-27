from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatPermissions


def restrict_member(update, context):
    update.message.reply_text(f"restrict_member : \n{update.effective_chat.restrict_member(user_id=update.effective_user.id, permissions=ChatPermissions(can_send_other_messages=True))}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', restrict_member))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
