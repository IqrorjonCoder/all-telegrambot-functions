from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def revoke_invite_link(update, context):
    update.message.reply_text(f"revoke_invite_link : \n{update.effective_chat.revoke_invite_link(invite_link='https://t.me/+tqRYTgc1tTEyNjky')}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', revoke_invite_link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
