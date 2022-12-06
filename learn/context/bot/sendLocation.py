from telegram.ext import Updater, CommandHandler


def sendLocation(update, context):
    context.bot.sendLocation(chat_id=update.effective_chat.id,
                              latitude=12.123,
                              longitude=13.123)


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendLocation))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()