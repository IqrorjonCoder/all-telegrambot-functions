from telegram.ext import Updater, CommandHandler


def edit_message_caption(update, context):
    context.bot.edit_message_caption(chat_id=update.effective_chat.id,
                                     message_id=update.message.message_id-1,
                                     caption="changed !!!")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', edit_message_caption))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()