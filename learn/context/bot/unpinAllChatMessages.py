from telegram.ext import Updater, CommandHandler


def unpinAllChatMessages(update, context):
    x = context.bot.unpinAllChatMessages(chat_id=update.effective_chat.id)
    update.message.reply_text(f"unpinAllChatMessages : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unpinAllChatMessages))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
