from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import LabeledPrice


def send_invoice(update, context):
    update.effective_chat.send_invoice(title="this is an example payment",
                                       description="this is an example description",
                                       payload="coupon",
                                       provider_token="398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065",
                                       currency="uzs",
                                       prices=[LabeledPrice(label="simple payment", amount=100000)],
                                       photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-H9c7MTeguHW9AosDLVb4oOc1cNn8xdWISmygke-R&s")
    update.message.reply_text(f"send_invoice : \n{123}")


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_invoice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
