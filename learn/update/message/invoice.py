from telegram.ext import Updater, CommandHandler
from telegram import Invoice, LabeledPrice


def invoice(update, context):
    update.message.reply_text("salom ...")
    update.message.reply_invoice(Invoice(title="exmaple title",
                                         description="ex. description",
                                         start_parameter="salom",
                                         currency="currancy",
                                         total_amount=100))



def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', invoice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()