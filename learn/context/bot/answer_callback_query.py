from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

states = {
    "callback": 1
}


def start(update, context):
    update.message.reply_text("salom", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("one", callback_data="one")],
                                                                          [InlineKeyboardButton("two", callback_data="two")]]))
    return states["callback"]


def answer_callback_query(update, context):
    print(update.callback_query)
    context.bot.answer_callback_query(callback_query_id=str(update.callback_query.id),
                                      text=f"you clicked {update.callback_query.data}",
                                      show_alert=True)

    #delete message after clicked the any of inline buttons
    # context.bot.delete_message(chat_id=update.callback_query.message.chat_id,
    #                            message_id=update.callback_query.message.message_id)
    return ConversationHandler.END


def runner():
    updater = Updater(token="5333086108:AAGY1trMmjcIoFHcexHxCUfN_atAdgKwJ0s")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [CallbackQueryHandler(answer_callback_query)],
        },
        fallbacks=[CommandHandler('start', start)]
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
