from telegram.ext import Updater, CommandHandler


def logOut(update, context):
    update.message.reply_text(f"bot logOut : \n\n{context.bot.logOut}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', logOut))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()