from telegram.ext import Updater, CommandHandler


def setStickerSetThumb(update, context):
    x = context.bot.setStickerSetThumb(name='stickerset_name ',
                                          user_id=update.effective_user.id)
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', setStickerSetThumb))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()