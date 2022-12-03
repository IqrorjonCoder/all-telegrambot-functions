from telegram.ext import Updater, CommandHandler


def delete_chat_photo(update, context):
    update.message.reply_text(f"{context.bot.delete_chat_photo(chat_id=update.effective_chat.id)}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', delete_chat_photo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()