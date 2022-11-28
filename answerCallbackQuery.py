from telegram.ext import Updater, MessageHandler, CommandHandler, ConversationHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


states = {
    "callback": 1,
}



def start(update, context):
    update.message.reply_text("salomcha ...", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("one", callback_data="one")],
                                                                                 [InlineKeyboardButton("two", callback_data="two")]]))
    return states["callback"]


def answerCallbackQuery(update, context):
    context.bot.answerCallbackQuery(callback_query_id=update.callback_query.id,
                                    text=f"you selected this : {update.callback_query.data}",
                                    show_alert=True)



def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [CallbackQueryHandler(answerCallbackQuery)]
        },
        fallbacks=[CommandHandler('stop', start)],
        per_message=False,
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()