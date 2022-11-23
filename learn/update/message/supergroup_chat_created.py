from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def supergroup_chat_created(update, context):
    update.message.reply_text(f"supergroupchat created is :  {update.message.supergroup_chat_created}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', supergroup_chat_created))
    # dispatcher.add_handler(MessageHandler(Filters.status_update.chat_created, supergroup_chat_created))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()

