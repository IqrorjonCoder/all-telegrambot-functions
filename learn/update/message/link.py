from telegram.ext import Updater, CommandHandler
from telegram import Invoice, LabeledPrice


def link(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_text(f"you *{update.message.text}* message link is : \n{update.message.link}", parse_mode="Markdown")


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', link))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()