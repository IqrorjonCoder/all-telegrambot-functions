from telegram.ext import Updater, CommandHandler
from telegram import LabeledPrice


def send_invoice(update, context):
    update.message.reply_text("salom ...")
    update.effective_user.send_invoice(title="simple payment example",
                                       description="this is an example payment",
                                       payload="coupon",
                                       provider_token="398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065",
                                       currency="uzs",
                                       prices=[LabeledPrice(label="10 ming summ", amount=1000 * 100)],
                                       photo_url="https://cdn.lifehacker.ru/wp-content/uploads/2022/06/a9c2fcca-1a23-41e9-a18a-43a4beee4709-kopiya_1654586421.jpg",
                                       photo_width=1000,
                                       photo_size=1000,
                                       need_name=True,
                                       need_phone_number=True,
                                       )



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_invoice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()