from telegram.ext import Updater, CommandHandler


def declineChatJoinRequest(update, context):
    context.bot.declineChatJoinRequest(chat_id=update.effective_chat.id,
                                          user_id=update.effective_user.id,)



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', declineChatJoinRequest))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()