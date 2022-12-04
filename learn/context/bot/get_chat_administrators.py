from telegram.ext import Updater, CommandHandler


def get_chat_administrators(update, context):
    chat_mem = context.bot.get_chat_administrators(chat_id=update.effective_chat.id)
    for i in chat_mem:
        update.message.reply_text(f"{i.to_json()}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_chat_administrators))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()