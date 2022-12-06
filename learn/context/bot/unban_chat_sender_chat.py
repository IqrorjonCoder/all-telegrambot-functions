from telegram.ext import Updater, CommandHandler


def unban_chat_sender_chat(update, context):
    x = context.bot.unban_chat_sender_chat(chat_id=update.effective_chat.id,
                                           sender_chat_id=1397003436)
    update.message.reply_text(f"unban_chat_sender_chat : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unban_chat_sender_chat))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
