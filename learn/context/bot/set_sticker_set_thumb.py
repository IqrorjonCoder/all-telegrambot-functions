from telegram.ext import Updater, CommandHandler


def set_sticker_set_thumb(update, context):
    x = context.bot.set_sticker_set_thumb(name='stickerset_name ',
                                          user_id=update.effective_user.id)
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_sticker_set_thumb))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()