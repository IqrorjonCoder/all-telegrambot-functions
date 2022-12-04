from telegram.ext import Updater, CommandHandler


def get_chat(update, context):
    chat = context.bot.get_chat(chat_id=update.effective_chat.id)
    update.message.reply_text(f"{chat}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()