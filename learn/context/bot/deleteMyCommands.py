from telegram.ext import Updater, CommandHandler
from telegram import BotCommandScope


def deleteMyCommands(update, context):
    print(context.bot.deleteMyCommands(scope=BotCommandScope.DEFAULT))



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', deleteMyCommands))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()