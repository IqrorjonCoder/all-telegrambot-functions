from telegram.ext import Updater, CommandHandler


def setWebhook(update, context):
    # x = context.bot.setWebhook()
    update.message.reply_text(f"webhook")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', setWebhook))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()