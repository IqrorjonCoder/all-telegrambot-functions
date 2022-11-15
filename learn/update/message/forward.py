from telegram.ext import Updater, CommandHandler


def forward(update, context):
    update.message.reply_text("salom ...")
    # 1035463819
    # -1001609283019
    print(update.message.chat_id)
    update.message.forward(chat_id=-1001609283019)
    # context.bot.forward_message(chat_id=1035463819,
    #                             from_chat_id=-1001609283019,
    #                             message_id=update.effective_message.message_id)


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', forward))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()