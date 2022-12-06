from telegram.ext import Updater, CommandHandler
from telegram import LabeledPrice


def sendInvoice(update, context):
    context.bot.sendInvoice(chat_id=update.effective_chat.id,
                             title="simple title",
                             description="simplee description",
                             payload="coupon",
                             provider_token="398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065",
                             currency="uzs",
                             prices=[LabeledPrice('simplee label', 10000)])


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendInvoice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()