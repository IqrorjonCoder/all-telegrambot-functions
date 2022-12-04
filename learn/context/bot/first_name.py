from telegram.ext import Updater, CommandHandler


def first_name(update, context):
    update.message.reply_text(f"first name : {context.bot.first_name}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', first_name))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()