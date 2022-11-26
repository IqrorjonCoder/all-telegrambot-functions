from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup


def mention_button(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"Come on my profile !", reply_markup=InlineKeyboardMarkup([[update.effective_user.mention_button(name="come on!")]]))



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', mention_button))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()