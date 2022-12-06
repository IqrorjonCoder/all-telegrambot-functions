from telegram.ext import Updater, CommandHandler


def sendMessage(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id,
                             text="salomchaa ...")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendMessage))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()