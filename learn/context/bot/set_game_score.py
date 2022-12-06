from telegram.ext import Updater, CommandHandler


def set_game_score(update, context):
    x = context.bot.set_game_score(user_id=update.effective_user.id,
                                   score=100,
                                   chat_id=update.effective_chat.id,
                                   message_id=update.message.message_id-2)
    update.message.reply_text(f"changed  : {x}")



def runner():
    updater = Updater(token="5333086108:AAGOz98WcjgaJ5SEg208C_XS7rYVZJ8-eT4")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', set_game_score))

    updater.start_polling()
    updater.idle()



if __name__ == '__main__':
    print("ishga tushdi ...")
    runner()