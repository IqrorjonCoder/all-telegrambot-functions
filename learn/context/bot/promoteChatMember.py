from telegram.ext import Updater, CommandHandler


def promoteChatMember(update, context):
    x = context.bot.promoteChatMember(chat_id=update.effective_chat.id,
                                        user_id=update.effective_user.id,
                                        can_delete_messages=True)
    update.message.reply_text(f"promoteChatMember : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', promoteChatMember))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()