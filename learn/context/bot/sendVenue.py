from telegram.ext import Updater, CommandHandler


def sendVenue(update, context):
    context.bot.sendVenue(chat_id=update.effective_chat.id,
                           latitude=12.123,
                           longitude=13.123,
                           title="simplee title",
                           address="simplee address")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendVenue))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()