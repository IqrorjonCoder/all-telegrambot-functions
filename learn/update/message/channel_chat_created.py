from telegram.ext import Updater, CommandHandler


def channel_chat_created(update, context):
    update.message.reply_text("sallmom !!!")
    print(update.message.channel_chat_created)
    context.bot.send_message(chat_id=update.message.chat_id, text="salommm!!!!")


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', channel_chat_created))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()