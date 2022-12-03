from telegram.ext import Updater, CommandHandler


def close(update, context):
    update.message.reply_text(f"close : \n*{context.bot.close}*", parse_mode="Markdown")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', close))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()