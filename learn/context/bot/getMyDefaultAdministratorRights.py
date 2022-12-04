from telegram.ext import Updater, CommandHandler


def getMyDefaultAdministratorRights(update, context):
    cmds = context.bot.getMyDefaultAdministratorRights()
    update.message.reply_text(f"admin rights : \n\n{cmds}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', getMyDefaultAdministratorRights))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()