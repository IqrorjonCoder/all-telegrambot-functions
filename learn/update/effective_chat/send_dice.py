from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Dice


def send_dice(update, context):
    update.message.reply_text(f"send_dice : \n{update.effective_chat.send_dice(emoji=Dice.BOWLING)}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_dice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
