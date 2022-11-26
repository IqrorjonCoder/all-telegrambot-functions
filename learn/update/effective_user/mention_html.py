from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode


def mention_html(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"Come on my profile ! {update.effective_user.mention_html()}", parse_mode=ParseMode.HTML)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', mention_html))
    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, mention_html))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()