from telegram.ext import Updater, CommandHandler


def pinChatMessage(update, context):
    pin = context.bot.pinChatMessage(chat_id=update.effective_chat.id,
                                 message_id=update.message.message_id-1)
    update.message.reply_text(f"pinChatMessage : {pin}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', pinChatMessage))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()