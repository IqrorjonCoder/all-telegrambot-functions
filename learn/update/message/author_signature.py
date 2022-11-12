from telegram.ext import Updater, Filters, MessageHandler


def author_signature(update, context):
    update.message.reply_text("salomm")
    print(update.message.author_signature)


def runner():
    updater = Updater(token='5693888427:AAFE-_nYnUSOxtgDu-hXprZgUvyrLxS_KTE')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, author_signature))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishlamoqda ...")
    runner()
