from telegram.ext import Updater, CommandHandler


def kickChatMember(update, context):
    x = context.bot.kickChatMember(chat_id=update.effective_chat.id,
                                 user_id=update.effective_user.id)
    update.message.reply_text(f"kickChatMember : \n\n{x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', kickChatMember))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()