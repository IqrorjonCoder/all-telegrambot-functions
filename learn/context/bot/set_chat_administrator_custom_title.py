from telegram.ext import Updater, CommandHandler


def set_chat_administrator_custom_title(update, context):
    x = context.bot.set_chat_administrator_custom_title(chat_id=update.effective_chat.id,
                                                    user_id=1397003436,
                                                    custom_title="changed title")
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_chat_administrator_custom_title))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()