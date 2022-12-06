from telegram.ext import Updater, CommandHandler


def kick_chat_member(update, context):
    x = context.bot.kick_chat_member(chat_id=update.effective_chat.id,
                                 user_id=update.effective_user.id)
    update.message.reply_text(f"kick_chat_member : \n\n{x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', kick_chat_member))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()