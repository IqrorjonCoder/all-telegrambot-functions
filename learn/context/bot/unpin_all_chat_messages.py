from telegram.ext import Updater, CommandHandler


def unpin_all_chat_messages(update, context):
    x = context.bot.unpin_all_chat_messages(chat_id=update.effective_chat.id)
    update.message.reply_text(f"unpin_all_chat_messages : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unpin_all_chat_messages))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
