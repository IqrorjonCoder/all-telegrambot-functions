import datetime
from telegram.ext import Updater, CommandHandler
from telegram import LabeledPrice


def createInvoiceLink(update, context):
    link = context.bot.createInvoiceLink(title="simple title text !",
                                           description="simple description text !",
                                           payload="coupon",
                                           provider_token="398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065",
                                           currency="uzs",
                                           prices=[LabeledPrice("let's buy", 100000)])

    update.message.reply_text(f"link is : \n*{link}*", parse_mode="Markdown")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', createInvoiceLink))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()