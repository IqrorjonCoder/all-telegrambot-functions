from telegram.ext import Updater, Filters, MessageHandler, CommandHandler
from telegram import Dice

def reply_dice(update, context):

    # 1
    update.message.reply_dice(emoji=Dice.FOOTBALL)


def runner():
    updater = Updater(token="5333086108:AAHWOxN_ZQf0oBFKYC0MbIX0NRa0sRoPDlU")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', reply_dice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()