from telegram.ext import Updater, CommandHandler


def edit_text(update, context):
    print(update.message.message_id)
    update.message.reply_text("salom ....")
    # update.message.edit_text()

    context.bot.edit_message_text(chat_id=update.message.chat_id,
                                  message_id=update.message.message_id-1,
                                  text="changed text !!!")


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', edit_text))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print('ishga tushdi ...')
    runner()