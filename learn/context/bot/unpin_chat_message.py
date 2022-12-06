from telegram.ext import Updater, CommandHandler


def unpin_chat_message(update, context):
    x = context.bot.unpin_chat_message(chat_id=update.effective_chat.id,
                                       message_id=update.message.message_id-1)
    update.message.reply_text(f"unpin_chat_message : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unpin_chat_message))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
