from telegram.ext import Updater, CommandHandler


def ban_chat_member(update, context):
    context.bot.ban_chat_member(chat_id=update.effective_chat.id,
                                user_id=1397003436,)
    update.message.reply_text(f"banned chat member !!!")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('delete_user', ban_chat_member))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()