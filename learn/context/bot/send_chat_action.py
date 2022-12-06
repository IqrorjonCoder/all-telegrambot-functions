from telegram.ext import Updater, CommandHandler
from telegram import ChatAction


def send_chat_action(update, context):
    context.bot.send_chat_action(chat_id=update.effective_chat.id,
                                 action=ChatAction.RECORD_AUDIO)


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', send_chat_action))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()