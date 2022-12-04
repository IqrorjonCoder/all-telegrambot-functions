from telegram.ext import Updater, CommandHandler


def get_sticker_set(update, context):
    cmds = context.bot.get_sticker_set(name='stickersetname')
    update.message.reply_text(f"sticker set : \n\n{cmds}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_sticker_set))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()