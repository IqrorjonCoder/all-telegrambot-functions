from telegram.ext import Updater, CommandHandler


def bot(update, context):
    update.message.reply_text(f"bot : \n*{context.bot.bot}*", parse_mode="Markdown")
    print()



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', bot))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()