from telegram.ext import Updater, CommandHandler


def promote_chat_member(update, context):
    x = context.bot.promote_chat_member(chat_id=update.effective_chat.id,
                                        user_id=update.effective_user.id,
                                        can_delete_messages=True)
    update.message.reply_text(f"promote_chat_member : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', promote_chat_member))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()