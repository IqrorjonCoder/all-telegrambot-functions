from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, Location


def edit_live_location(update, context):
    print(update.message.message_id)
    context.bot.edit_message_live_location(chat_id=update.message.chat_id,
                                           message_id=456,
                                           location=Location(longitude=41.31375935883639, latitude=69.52833126736574))


def runner():
    updater = Updater(token='5693888427:AAFnCEAN51Jp3Tc74mIzUx9wXt2_IQDU0p8')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', edit_live_location))
    # dispatcher.add_handler(MessageHandler(Filters.location, edit_live_location))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print('ishga tushdi ...')
    runner()