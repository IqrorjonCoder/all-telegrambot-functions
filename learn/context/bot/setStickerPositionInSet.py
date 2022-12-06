from telegram.ext import Updater, CommandHandler


def setStickerPositionInSet(update, context):
    x = context.bot.setStickerPositionInSet(sticker='sticker',
                                                position=10)
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', setStickerPositionInSet))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()