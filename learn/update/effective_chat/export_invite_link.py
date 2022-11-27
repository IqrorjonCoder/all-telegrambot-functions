
from telegram.ext import Updater, CommandHandler


def export_invite_link(update, context):
    update.message.reply_text(f"""export_invite_link : \n{update.effective_chat.export_invite_link()}""")





def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', export_invite_link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()