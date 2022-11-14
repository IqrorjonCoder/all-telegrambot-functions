from telegram.ext import CommandHandler, Updater


def date(update, context):
    print(update.message.message_id)
    update.message.reply_text(f"the message is : *{update.message.text}*\n\n"
                              f"the message id : *{update.message.message_id}*\n\n"
                              f"message date is : *{update.message.date}*", parse_mode="Markdown")
    print(update.message.date)


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', date))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
