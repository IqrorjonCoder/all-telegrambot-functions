from telegram.ext import Updater, CommandHandler


def getGameHighScores(update, context):
    scores = context.bot.getGameHighScores(user_id=update.effective_user.id,
                                                 chat_id=update.effective_chat.id,
                                                 message_id=update.message.message_id-1)
    for i in scores:
        update.message.reply_text(f"{i.to_json()}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', getGameHighScores))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()