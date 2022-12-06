from telegram.ext import Updater, CommandHandler


def log_out(update, context):
    update.message.reply_text(f"bot log_out : \n\n{context.bot.log_out}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', log_out))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()