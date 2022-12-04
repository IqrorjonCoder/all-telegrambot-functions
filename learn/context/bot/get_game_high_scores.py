from telegram.ext import Updater, CommandHandler


def get_game_high_scores(update, context):
    print(update.message.message_id)
    scores = context.bot.get_game_high_scores(user_id=update.effective_user.id,
                                                 chat_id=update.effective_chat.id,
                                                 message_id=update.message.message_id-1)
    for i in scores:
        update.message.reply_text(f"{i.to_json()}")


def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', get_game_high_scores))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()