from telegram.ext import Updater, CommandHandler


def commands(update, context):
    update.message.reply_text(f"commands : \n*{[f'{i.to_json()}' for i in context.bot.commands]}*", parse_mode="Markdown")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', commands))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()