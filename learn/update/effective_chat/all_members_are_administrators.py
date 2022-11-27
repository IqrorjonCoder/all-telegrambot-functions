from telegram.ext import Updater, CommandHandler


def all_members_are_administrators(update, context):
    update.message.reply_text(f"all members are admin : {update.effective_chat.all_members_are_administrators}")



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', all_members_are_administrators))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()