from telegram.ext import Updater, CommandHandler


def insert_callback_data(update, context):
    update.message.reply_text(f"insert_callback_data : \n\n{context.bot.insert_callback_data(update)}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', insert_callback_data))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()