from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def forward_sender_name(update, context):
    update.message.reply_text(f"your message : \n{update.message.text}\n"
                              f"message id : {update.message.message_id}\n\n\n"
                              f"forward sender name : \n{update.message.forward_sender_name}")
    # 1035463819
    # -1001609283019
    print(update.message.chat_id)


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, forward_sender_name))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()