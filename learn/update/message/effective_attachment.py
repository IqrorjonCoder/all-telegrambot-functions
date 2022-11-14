from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def effective_attachment(update, context):
    update.message.reply_text(f"your message : \n\n{update.message.effective_attachment}")


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', effective_attachment))
    dispatcher.add_handler(MessageHandler(Filters.video, effective_attachment))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print('ishga tushdi ...')
    runner()