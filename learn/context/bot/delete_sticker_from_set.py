from telegram.ext import Updater, CommandHandler


def delete_sticker_from_set(update, context):
    print(context.bot.delete_sticker_from_set(sticker='🔥 File'))



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', delete_sticker_from_set))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()