from telegram.ext import Updater, CommandHandler


def forward_date(update, context):
    update.message.reply_text(f"your message : \n{update.message.text}\n\n\n"
                              f"forward date : {update.message.forward_date}")
    # 1035463819
    # -1001609283019
    print(update.message.chat_id)


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', forward_date))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()