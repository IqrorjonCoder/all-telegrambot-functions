from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

states = {
    "edit": 1,
}


def start(update, context):
    update.message.reply_document(document=open('/home/iqrorjon/PycharmProjects/all_telegrambot_functions/learn/context/bot/editMessageCaption.py', 'rb'), caption="this is unchanged caption!",
                                  reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("one", callback_data="one")],
                                                                     [InlineKeyboardButton("two", callback_data="two")]]))
    return states["edit"]


def editMessageCaption(update, context):
    query = update.callback_query
    context.bot.editMessageCaption(chat_id=query.message.chat_id,
                                     message_id=query.message.message_id,
                                     caption="changed caption !!!",
                                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("onee", callback_data="onee")],
                                                                     [InlineKeyboardButton("twoo", callback_data="twoo")]]))
    return ConversationHandler.END


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [CallbackQueryHandler(editMessageCaption)]
        },
        fallbacks=[CommandHandler('stop', start)]
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
