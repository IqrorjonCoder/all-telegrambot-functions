from telegram.ext import Updater, CommandHandler
from telegram import Dice


def send_dice(update, context):
    context.bot.send_dice(chat_id=update.effective_chat.id,
                          emoji=Dice.FOOTBALL)


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_dice))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()