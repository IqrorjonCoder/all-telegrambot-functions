from telegram.ext import Updater, CommandHandler
from telegram import PassportElementError


def setPassportDataErrors(update, context):
    x = context.bot.setPassportDataErrors(user_id=update.effective_user.id,
                                             errors=[
                                                 PassportElementError('sourse', 'typee', 'simplee error')
                                             ])
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', setPassportDataErrors))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()