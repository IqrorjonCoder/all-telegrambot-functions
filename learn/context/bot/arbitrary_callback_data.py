from telegram.ext import Updater, CommandHandler


def arbitrary_callback_data(update, context):
    update.message.reply_text(f"arbitrary_callback_data : {context.bot.arbitrary_callback_data}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', arbitrary_callback_data))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()