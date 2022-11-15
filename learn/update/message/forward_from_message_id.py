from telegram.ext import Updater, CommandHandler


def forward_from_message_id(update, context):
    update.message.reply_text(f"your message : \n{update.message.text}\n"
                              f"message id : {update.message.message_id}\n\n\n"
                              f"forward message id : \n{update.message.forward_from_message_id}")
    # 1035463819
    # -1001609283019
    print(update.message.chat_id)


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', forward_from_message_id))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()