from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def game(update, context):
    update.message.reply_text(f"your game : \n\n{update.message.game}")
    print(update.message.game)


def runner():
    updater = Updater(token="5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.game, game))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
