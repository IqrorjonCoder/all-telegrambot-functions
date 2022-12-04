from telegram.ext import Updater, CommandHandler


def get_webhook_info(update, context):
    user_pic = context.bot.get_webhook_info()
    update.message.reply_text(f"webhook info : \n\n{user_pic}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_webhook_info))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()