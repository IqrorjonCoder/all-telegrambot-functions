from telegram.ext import Updater, CommandHandler
from telegram import BotCommand


def set_my_commands(update, context):
    x = context.bot.set_my_commands(commands=[
        BotCommand('first', 'this is the first command'),
        BotCommand('second', 'this is the second command'),
    ])
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_my_commands))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()