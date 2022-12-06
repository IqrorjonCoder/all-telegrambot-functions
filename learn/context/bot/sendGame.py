from telegram.ext import Updater, CommandHandler


def sendGame(update, context):
    context.bot.sendGame(chat_id=update.effective_chat.id,
                          game_short_name="simplee game")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', sendGame))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()