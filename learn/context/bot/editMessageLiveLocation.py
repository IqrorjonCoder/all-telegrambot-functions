from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Location

states = {
    "edit": 1,
}


def start(update, context):
    location = Location(longitude=69.280070,
                        latitude=41.311436)
    context.bot.send_location(chat_id=update.effective_chat.id, location=location, live_period=100,
                              reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("one", callback_data="one")],
                                                                 [InlineKeyboardButton("two", callback_data="two")]]))

    return states["edit"]


def editMessageLiveLocation(update, context):
    location = Location(longitude=69.243329,
                        latitude=41.328583)
    query = update.callback_query
    context.bot.editMessageLiveLocation(chat_id=query.message.chat_id,
                                           message_id=query.message.message_id,
                                           location=location,
                                           reply_markup=InlineKeyboardMarkup(
                                               [[InlineKeyboardButton("onee", callback_data="onee")],
                                                [InlineKeyboardButton("twoo", callback_data="twoo")]]))
    return ConversationHandler.END


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [CallbackQueryHandler(editMessageLiveLocation)],
        },
        fallbacks=[CommandHandler('stop', start)]
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
