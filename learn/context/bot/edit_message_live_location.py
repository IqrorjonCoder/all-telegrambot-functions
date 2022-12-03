from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters


states = {
    "edit": 1,
}


def start(update, context):
    update.message.reply_location(longitude=19.123,
                                  latitude=20.123)
    return states["edit"]


def edit_message_live_location(update, context):
    context.bot.edit_message_live_location(chat_id=update.effective_chat.id,
                                           message_id=update.message.message_id-1,
                                           latitude=12.123,
                                           longitude=13.123)
    return ConversationHandler.END

def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    # dispatcher.add_handler(CommandHandler('start', edit_message_live_location))

    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [MessageHandler(Filters.text, edit_message_live_location)],
        },
        fallbacks=[MessageHandler(Filters.location, start)]
    ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()