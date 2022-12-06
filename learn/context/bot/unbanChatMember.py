from telegram.ext import Updater, CommandHandler


def unbanChatMember(update, context):
    x = context.bot.unbanChatMember(chat_id=update.effective_chat.id,
                                      user_id=1397003436)
    update.message.reply_text(f"unbanChatMember : {x}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', unbanChatMember))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()
