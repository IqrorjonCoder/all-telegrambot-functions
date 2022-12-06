from telegram.ext import Updater, CommandHandler


def sendPoll(update, context):
    context.bot.sendPoll(chat_id=update.effective_chat.id,
                          question="where are you from ?",
                          options=[
                              "Uzbekistan",
                              "USA",
                              "UK"
                          ])


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendPoll))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()