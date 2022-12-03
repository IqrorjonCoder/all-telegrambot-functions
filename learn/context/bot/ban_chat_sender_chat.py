from telegram.ext import Updater, CommandHandler


def ban_chat_sender_chat(update, context):
    context.bot.ban_chat_sender_chat(chat_id=update.effective_chat.id, sender_chat_id=update.effective_chat.id)
    update.message.reply_text(f"ban chat sender chat !!!")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', ban_chat_sender_chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()