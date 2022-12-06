from telegram.ext import Updater, CommandHandler


def leave_chat(update, context):
    x = context.bot.leave_chat(chat_id=update.effective_chat.id)
    update.message.reply_text(f"bot leave_chat : \n\n{x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', leave_chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()