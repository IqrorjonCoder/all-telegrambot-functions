from telegram.ext import Updater, CommandHandler
from telegram import ParseMode


def mention_markdown(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"Come on my profile ! {update.effective_user.mention_markdown()}", parse_mode=ParseMode.MARKDOWN)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', mention_markdown))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()