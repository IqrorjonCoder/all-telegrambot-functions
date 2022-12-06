from telegram.ext import Updater, CommandHandler


def to_dict(update, context):
    update.message.reply_text(f"to_dict : {context.bot.to_dict()}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', to_dict))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()