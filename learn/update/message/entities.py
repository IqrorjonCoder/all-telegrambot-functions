from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def entities(update, context):
    update.message.reply_text(f"your message : \n\n{update.message.text}\n\n\n\n\n"
                              f"entities : \n")
    for i in update.message.entities:
        update.message.reply_text(i.to_json())


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', entities))
    dispatcher.add_handler(MessageHandler(Filters.text, entities))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print('ishga tushdi ...')
    runner()