from telegram.ext import Updater, CommandHandler


def getWebhookInfo(update, context):
    web_h = context.bot.getWebhookInfo()
    update.message.reply_text(f"webhook info : \n\n{web_h}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', getWebhookInfo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()