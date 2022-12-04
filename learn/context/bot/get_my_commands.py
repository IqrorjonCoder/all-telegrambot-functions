from telegram.ext import Updater, CommandHandler


def get_my_commands(update, context):
    cmds = context.bot.get_my_commands()
    for i in cmds:
        update.message.reply_text(f"{i.to_json()}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_my_commands))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()