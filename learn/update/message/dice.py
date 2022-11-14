from telegram.ext import Updater, CommandHandler
from telegram import Dice


def dice(update, context):
    update.message.reply_text("salom ...")
    # update.message.dice(Dice(value=2, emoji='🎯'))
    context.bot.send_dice(chat_id=update.message.chat_id, emoji="🏀")


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', dice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
