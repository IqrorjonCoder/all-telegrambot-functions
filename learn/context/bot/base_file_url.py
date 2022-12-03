from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def base_file_url(update, context):
    update.message.reply_text("photo...")
    print(context.bot.base_file_url)



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.photo, base_file_url))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()