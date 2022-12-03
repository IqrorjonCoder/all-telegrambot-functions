from telegram.ext import Updater, CommandHandler


def deleteStickerFromSet(update, context):
    print(context.bot.deleteStickerFromSet(sticker='🔥 File'))



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', deleteStickerFromSet))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()