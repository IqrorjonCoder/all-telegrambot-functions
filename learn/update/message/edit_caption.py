from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def edit_caption(update, context):
    print(update.message.message_id)
    update.message.reply_text("salom ...")
    # context.bot.edit_message_caption(chat_id=update.message.chat_id,
    #                                  message_id=423,
    #                                  caption="salommmm this")

    update.message.edit_caption(caption="salommmm this")

def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', edit_caption))
    dispatcher.add_handler(MessageHandler(Filters.animation, edit_caption))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print('ishga tushdi ...')
    runner()